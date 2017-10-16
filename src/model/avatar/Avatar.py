# Avatar.py

from model.core.Agent import Agent
from model.avatar.AvatarControls import Controls
from model.avatar.Bonus import Bonus
from collections import deque

class Avatar(Agent):
    """
    The agent Avatar

    an agent have a position in the environement, contain a pointer to the environment and a traceFile to log information. it decide to move at a frequency determined by the user. The user chose the direction where the avatar have to move.
    """

    
    def __init__(self, environment, posX, posY, tick, time_bonus, reward, trace_file=None):
        """ Initialize the Agent
        
        set its view representation (color, form)
  
        :param environment: pointer to the environment where the agent live
        :param posX: abscissa coordinate of the agent
        :param posY: ordinate coordinate of the agent
        :param tick: frequency of decision, the agent only decide after [tick] turn of decision
        :param time_bonus: a bonus is active for [time_bonus] turn 
        :param reward: number of bonus which need to be catch to win the game
        :trace_file: file to write the log information (default = None)
        """
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.color = 'red'
        self.next_controls = deque([])
        self.move = Controls.UP
        self.tick = tick
        self.cpt = 1
        self.cpt_reverse = -1
        self.point = 0
        self.time_bonus = time_bonus
        self.reward = reward

    def decide(self):
        """ decision process of the Avatar """
        if self.cpt%self.tick == 0:
            self.cpt = 1

            if len(self.next_controls):
                self.move = self.next_controls.popleft()

            x = 0
            y = 0
            if self.move == Controls.RIGHT:
                x = 1
            elif self.move == Controls.LEFT:
                x = -1
            elif self.move == Controls.UP:
                y = -1
            elif self.move == Controls.DOWN:
                y = 1

            newX = 0
            newY = 0
            newX, newY = self.environment.compute_new_position(self.posX, self.posY, x, y)
            if self.environment.is_in(newX, newY) and isinstance(self.environment.get_agent(newX, newY), Bonus):
                self.environment.reverse_hunter = True
                self.cpt_reverse = self.time_bonus
                self.environment.move_agent(self, newX, newY)
                self.point += 1
            elif self.environment.can_move(newX, newY):
                self.environment.move_agent(self, newX, newY)

            self.environment.update_target()

        self.cpt += 1
        self.cpt_reverse -= 1
        if self.cpt_reverse == 0:
            self.environment.reverse_hunter = False
        if self.point == self.reward:
            return True
        return False

    def new_move(self, move):
        """ function used by the AvatarControl class to send the next direction that the avatar has to follow

        :param move: direction LEFT -> 1, RIGHT -> 2, UP -> 3, DOWN -> 4
        :type move: int
        """
        self.next_controls.append(move)
