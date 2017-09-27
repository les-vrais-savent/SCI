# Fish.py

from core.Agent import Agent

class Fish(Agent):

    """ Constructeur du poisson """
    def __init__(self, id, environment, pasX, pasY, posX, posY, fishBreedTime, trace_file=None):
        Agent.__init__(self, id, environment, pasX, pasY, posX, posY, trace_file)
        self.fishBreedTime = fishBreedTime
        self.fishCounter = 0

    """ Décision """
    def decide(self):
        """ Mouvement  """
        

        """ Gestation """
        self.fishCounter += 1

        if self.fishCounter == self.fishBreedTime:
            self.fishCounter = 0
            # add agent
 
        return
