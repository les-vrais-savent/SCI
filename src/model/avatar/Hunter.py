# Hunter.py

from model.core.Agent import Agent
from model.avatar.Avatar import Avatar

class Hunter(Agent):

    def __init__(self, environment, posX, posY, tick, trace_file=None):
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.color = 'blue'
        self.tick = tick 
        self.cpt = 1

    def decide(self):
        if self.cpt%self.tick == 0:
            self.cpt = 1
            x, y = self.environment.get_next_position(self)
            dead_avatar = False
            if isinstance(self.environment.get_agent(x, y), Avatar):
                dead_avatar = True
            self.environment.move_agent(self, x, y)
            return dead_avatar 
        self.cpt += 1
        return False

