# Fish.py

from model.wator.Animal import Animal
import random

class Fish(Animal):
    """ a Fish agent

    this agent do random move on the environment and produce other Fish  with a given period
    """
    
    def __init__(self, environment, posX, posY, breedTime, trace_file=None):
        """ Initialize the Fish
        
        :param environment: pointer to the environment where the agent live
        :param posX: abscissa coordinate of the agent
        :param posY: ordinate coordinate of the agent
        :param breedTime: the Shark produce a new Shark after [breedTime] turn
        :trace_file: file to write the log information (default = None)
        """
        
        Animal.__init__(self, environment, posX, posY, breedTime, trace_file)
        self.color = 'steel blue'

    def lay_egg(self, posX, posY):
        """  produce a Fish to the position posX, posY """
        # """
        # if self.trace_file != None:
        #     self.trace_file.write('Fish position : ' + str(self.posX) +
        #                           ',' + str(self.posY) +
        #                           ' lay egg at position : ' + str(posX) +
        #                           ',' + str(posY) + '\n')
        # """                   
        return Fish(self.environment, posX, posY, 3, self.trace_file)

    def getColor(self):
        """ return the Fish color, depend of turn it was created

        :return: if the fish was create at this turn return deep sky blue, return steel blue otherwise
        """
        if self.baby:
            self.baby = False
            return 'deep sky blue'
        return self.color
    
    def decide(self):
        """ decision process of the Fish """
        if not self.alive:
            return
        self.moved = False
        lastX = self.posX
        lastY = self.posY

        # Mouvement
        self.moved = self.random_move()

        # Gestation
        self.gestation(lastX, lastY)
        return
