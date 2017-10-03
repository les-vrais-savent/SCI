# Avatar.py

from model.core.Agent import Agent

class Avatar(Agent):

    def __init__(self, environment, posX, posY, trace_file=None):
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.color = 'yellow'

    def decide(self):
        x, y = self.environment.get_next_position(self)
        self.environment.move_agent(self, x, y)
        return
