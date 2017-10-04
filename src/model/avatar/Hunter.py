# Hunter.py

from model.core.Agent import Agent

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
            self.environment.move_agent(self, x, y)
            return
        self.cpt += 1
        return

