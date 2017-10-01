# Agent.py
import random

next_id = 1

class Agent:

    def __init__(self, environment, pasX, pasY, posX, posY, trace_file=None):
        global next_id
        self.id = next_id 
        next_id += 1
        self.color = 'blue'
        self.environment = environment
        self.pasX = pasX
        self.pasY = pasY
        self.posX = posX
        self.posY = posY
        self.trace_file = trace_file
        self.ticks = 0;

    def __str__(self):
        return str(self.id)

    # def neighborhood_coord(self):
    #     return self.environment.neighborhood_coord(self.posX,
    #                                                 self.posY)
    
    """
    essai de déplacer l'agent aléatoirement dans les direction haut, bas, droite, gauche. 
    S'il y arrive, renvoie True, 
    Sinon (l'agent est encerclé) renvoie False
    """
    def random_move(self):
        possiblesMov = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        random.shuffle(possiblesMov)        
        
        for x, y in possiblesMov:
            if self.environment.can_move(self.posX, self.posY, x, y):
                self.posX, self.posY = self.environment.move_agent(self.posX, self.posY, x, y)
                return True
        
        return False
    
    def decide(self):
        return
