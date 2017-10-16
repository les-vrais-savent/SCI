from model.avatar.Hunter import Hunter
from model.core.Agent import Agent
import random

class BonusHunter(Hunter):
        def __init__(self, environment, posX, posY, tick, trace_file=None):
            Hunter.__init__(self, environment, posX, posY, tick, trace_file)
            self.reverse = False
            self.init_color = 'yellow'

            
        def move(self, move, distance):
            env = self.environment
            if distance > 10:
                self.init_color= 'yellow'
                return False
            else:
                self.init_color= 'blue'
                return self.simple_move(move)
