# Fish.py

from model.core.Agent import Agent
import random

class Fish(Agent):

    """ Constructeur du poisson """
    def __init__(self, environment, pasX, pasY, posX, posY, fishBreedTime, trace_file=None):
        Agent.__init__(self, environment, pasX, pasY, posX, posY, trace_file)
        self.fishBreedTime = fishBreedTime
        self.fishCounter = 0
        self.color = 'blue'

    """ Décision """
    def decide(self):
        moved = False

        """ Mouvement  """
        possiblesMov = [(-1, 0), (0, -1), (1, 0), (0, 1)] 
        random.shuffle(possiblesMov)

        lastX = self.posX
        lastY = self.posY

        for x, y in possiblesMov:
            if self.environment.can_move(self.posX, self.posY, x, y):
                self.posX, self.posY = self.environment.move_agent(self.posX, self.posY, x, y)
                moved = True
                break

        """ Gestation """
        self.fishCounter += 1

        if self.fishCounter == self.fishBreedTime:
            self.fishCounter = 0
            if moved:
                self.environment.put_agent(Fish(self.environment,
                                                random.randint(-1,1),
                                                random.randint(-1,1),
                                                lastX, lastY, 3, self.trace_file))

        return
