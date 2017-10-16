# Wall.py

from model.core.Agent import Agent

class Wall(Agent):
    """
    A static agent. its color is white and its form is square
    """
    def __init__(self, environment, posX, posY, trace_file=None):
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.color = 'white'
        self.form = 'rect'

    def decide(self):
        return
