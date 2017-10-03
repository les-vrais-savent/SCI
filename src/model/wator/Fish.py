# Fish.py

from model.wator.Animal import Animal
import random

class Fish(Animal):

    """ Constructeur du poisson """
    def __init__(self, environment, posX, posY, breedTime, trace_file=None):
        Animal.__init__(self, environment, posX, posY, breedTime, trace_file)
        self.color = 'steel blue'

    def lay_egg(self, posX, posY):
        """
        if self.trace_file != None:
            self.trace_file.write('Fish position : ' + str(self.posX) +
                                  ',' + str(self.posY) +
                                  ' lay egg at position : ' + str(posX) +
                                  ',' + str(posY) + '\n')
        """                   
        return Fish(self.environment, posX, posY, 3, self.trace_file)

    def getColor(self):
        if self.baby:
            self.baby = False
            return 'deep sky blue'
        return self.color
    
    """ Décision """
    def decide(self):
        if not self.alive:
            return
        self.moved = False
        lastX = self.posX
        lastY = self.posY
        
        """ Mouvement  """
        self.moved = self.random_move()

        """ Gestation """
        self.gestation(lastX, lastY)
        return
