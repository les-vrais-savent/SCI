# Shark.py

from model.core.Agent import Agent
import random

class Shark(Agent):

    """ Constructeur du requin """
    def __init__(self, environment, pasX, pasY, posX, posY, lifeTime, sharkBreedTime, trace_file=None):
        Agent.__init__(self, environment, pasX, pasY, posX, posY, trace_file)
        self.lifeTime = lifeTime
        self.sharkBreedTime = sharkBreedTime
        self.sharkCounter = 0
        self.lifeCounter = 0 # Si = lifeTime, alors il meurt
        self.color = 'black'

    """ Décision """
    def decide(self):
        moved = False
        self.lifeCounter += 1

        """ Mouvement """
        possiblesMov = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        random.shuffle(possiblesMov) 

        lastX = self.posX
        lastY = self.posY

        """ Radar autours du requin pour détecter un poisson """
        for x, y in possiblesMov:
            neighbour = self.environment.get_agent(x, y)
            if type(neighbour) == Shark or neighbour == None:
                continue
            else:
                """ C'est un poisson, on le mange """
                moved = True
                self.environment.remove_agent(neighbour)
                self.posX, self.posY = self.environment.move_agent(self.posX, self.posY, x, y)
                self.lifeCounter = 0
                break

        """ S'il n'a pas mangé, il bouge aléatoirement """
        if not moved:
            for x, y in possiblesMov:
                if self.environment.can_move(self.posX, self.posY, x, y):
                    self.posX, self.posY = self.environment.move_agent(self.posX, self.posY, x, y)
                    moved = True
                    break

        """ Gestation """
        self.sharkCounter += 1

        if self.sharkCounter == self.sharkBreedTime:
            self.sharkCounter = 0
            if moved:
                self.environment.put_agent(Shark(self.environment,
                                                 random.randint(-1,1),
                                                 random.randint(-1,1),
                                                 lastX, lastY, 5, 3, self.trace_file))
