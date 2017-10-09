# Avatar.py

from model.core.Agent import Agent
from model.avatar.AvatarControls import Controls
from model.avatar.Bonus import Bonus
from collections import deque

class Avatar(Agent):

    def __init__(self, environment, posX, posY, tick, time_bonus, reward, trace_file=None):
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
                self.environment.reverse_hunter = not self.environment.reverse_hunter
                self.cpt_reverse = self.time_bonus
                self.environment.move_agent(self, newX, newY)
                self.point += 1
            elif self.environment.can_move(newX, newY):
                self.environment.move_agent(self, newX, newY)

            self.environment.update_target()

        self.cpt += 1
        self.cpt_reverse -= 1
        if self.cpt_reverse == 0:
            self.environment.reverse_hunter = not self.environment.reverse_hunter
        if self.point == self.reward:
            return True
        return False

    def new_move(self, move):
        self.next_controls.append(move)
