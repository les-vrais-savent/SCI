# Hunter.py

from model.core.Agent import Agent
from model.avatar.Avatar import Avatar

class Hunter(Agent):
    """
    The agent Hunter

    an agent have a position in the environement, contain a pointer to the environment and a traceFile to log information. it decide to move at a frequency determined by the user. It try to bring him closer to the Avatar and can destroy it.
    """
    
    def __init__(self, environment, posX, posY, tick, trace_file=None):
         """ Initialize the Agent
        
        set its view representation (color, form)
  
        :param environment: pointer to the environment where the agent live
        :param posX: abscissa coordinate of the agent
        :param posY: ordinate coordinate of the agent
        :param tick: move frequency, the agent move only after [tick] turn
        :trace_file: file to write the log information (default = None)
        """
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.color = 'blue'
        self.init_color = 'blue'
        self.tick = tick 
        self.cpt = 1


    def simple_move(self, move):
        """ move the hunter 

        use the environement to chose the position which bring him closer to the avatar

        :return: True if the hunter moved on a position that contained the avatar, False otherwise
        """
        x,y = move
        dead_avatar = isinstance(self.environment.get_agent(x, y), Avatar)
        self.environment.move_agent(self, x, y) 
        return dead_avatar

    def move(self, move, distance):
        """ make the Hunter move"""
        return self.simple_move(move)
    
    def decide(self):
        """ decision process of the Hunter """
        if self.cpt%self.tick == 0:
            self.cpt = 1
            dead_avatar = False
            (move,distance) = self.environment.get_next_position(self, self.environment.gridDJ, self.environment.reverse_hunter)

            if move != None:
                dead_avatar = self.move(move, distance)
                if self.environment.reverse_hunter:
                    self.color = 'purple'
                else:
                    self.color= self.init_color
                return dead_avatar
        self.cpt += 1
        return False
