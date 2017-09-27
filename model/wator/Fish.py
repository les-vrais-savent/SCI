# Fish.py

from core.Agent import Agent
import random

class Fish(Agent):

    """ Constructeur du poisson """
    def __init__(self, id, environment, pasX, pasY, posX, posY, fishBreedTime, trace_file=None):
        Agent.__init__(self, id, environment, pasX, pasY, posX, posY, trace_file)
        self.fishBreedTime = fishBreedTime
        self.fishCounter = 0

    """ Décision """
    def decide(self):
        moved = False

        """ Mouvement  """
        possiblesMov = [(-1, 0), (0, -1), (1, 0), (0, 1)] 
        random.shuffle(possibles_mov)

        for x, y in possibles_mov:
            if self.environment.can_move(self.posX, self.posY, x, y):
                self.posX, self.posY = self.environment.move_agent(self.posX, self.posY, x, y)
                moved = True
                break

        """ Gestation """
        self.fishCounter += 1

        if self.fishCounter == self.fishBreedTime:
            self.fishCounter = 0
            #if moved:
            #    self.environment.put_agent(Fish(

        return
