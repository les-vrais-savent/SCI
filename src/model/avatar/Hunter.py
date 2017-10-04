# Hunter.py

from model.core.Agent import Agent

class Hunter(Agent):

    def __init__(self, environment, posX, posY, trace_file=None):
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.color = 'blue'
        self.tick = 10
        self.cpt = 0

    def decide(self):
        if self.cpt%self.tick == 0:
            self.cpt = 0
            return
        self.cpt += 1
        x, y = self.environment.get_next_position(self)
        self.environment.move_agent(self, x, y)
        return
