# Hunter.py

from model.core.Agent import Agent
from model.avatar.Avatar import Avatar

class Hunter(Agent):

    def __init__(self, environment, posX, posY, tick, trace_file=None):
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.color = 'blue'
        self.init_color = 'blue'
        self.tick = tick 
        self.cpt = 1

    """
    déplace le Hunter, renvoi True s'il a tuer l'avatar, False sinon
    """
    def simple_move(self, move):
        x,y = move
        dead_avatar = isinstance(self.environment.get_agent(x, y), Avatar)
        self.environment.move_agent(self, x, y) 
        return dead_avatar

    def move(self, move, distance):
        return self.simple_move(move)
    
    def decide(self):
        if self.cpt%self.tick == 0:
            self.cpt = 1
            dead_avatar = False
            (move,distance) = self.environment.get_next_position(self, self.environment.gridDJ, self.environment.reverse_hunter)

            if move != None:
                dead_avatar = self.move(move, distance)
                if self.environment.reverse_hunter:
                    self.color = 'lemon chiffon'
                else:
                    self.color= self.init_color
                return dead_avatar
        self.cpt += 1
        return False
