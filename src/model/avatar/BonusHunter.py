from model.avatar.Hunter import Hunter
from model.core.Agent import Agent
import random

class BonusHunter(Hunter):
    """
    The agent BonusHunter

    Child of Hunter class, overide the move method to stay at the same position if the avatar is too far
    """
    def __init__(self, environment, posX, posY, tick, trace_file=None):
        Hunter.__init__(self, environment, posX, posY, tick, trace_file)
        self.reverse = False
        self.init_color = 'yellow'

    def move(self, move, distance):
        """ if the distance between the BonusHunter and the Avatar is highter than 10, just return False and set its color to yellow, otherwise, move like a Hunter and set its color to blue
        """
        env = self.environment
        if distance > 10:
            self.init_color= 'yellow'
            return False
        else:
            self.init_color= 'blue'
            return self.simple_move(move)
