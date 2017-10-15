# Shark.py

from model.wator.Animal import Animal
import random

class Shark(Animal):
    """ a Shark agent

    this agent eats Fish agent and can die if it didn't eat since a given time. produce other Shark with a given period
    """

    def __init__(self, environment, posX, posY, lifeTime, breedTime, trace_file=None):
        """ Initialize the Shark
        
        :param environment: pointer to the environment where the agent live
        :param posX: abscissa coordinate of the agent
        :param posY: ordinate coordinate of the agent
        :param lifeTime: after [lifetime] turn sin eat, the Shark die
        :param breedTime: the Shark produce a new Shark after [breedTime] turn
        :trace_file: file to write the log information (default = None)
        """
        Animal.__init__(self, environment, posX, posY, breedTime, trace_file)
        self.lifeTime = lifeTime
        self.lifeCounter = 0 # Si = lifeTime, alors il meurt
        self.color = 'black'

    def getColor(self):
        """ return the Shark color, depend of turn it was created

        :return: if the shark was create at this turn return gray, return black otherwise
        """
        if self.baby:
            self.baby = False
            return 'gray'
        return self.color

    """
    essai de manger un poisson autour de lui
    renvoi True s'il y arrive
    False sinon
    """
    def eat(self):
        """ look for fish around the Shark and eat it

        ask the environment if their are fish next to the Shark if there is a Fish, ask the environment to delete it.

        :return: True if the Shark found a Fish and eated it. False otherwise
        """

        lastX = self.posX
        lastY = self.posY
        
        possiblesMov = [(-1, 0), (0, -1), (1, 0), (0, 1)]        
        random.shuffle(possiblesMov)

        # Radar autours du requin pour détecter un poisson
        for x, y in possiblesMov:
            movX, movY = self.environment.compute_new_position(
                self.posX, self.posY, x, y)
            
            neighbour = self.environment.get_agent(movX, movY)
            if type(neighbour) == Shark or neighbour == None:
                continue
            else:
                # C'est un poisson, on le mange 
                # """
                # if self.trace_file != None:
                #     self.trace_file.write("Shark : " + str(self.id) + " eat fish : " + str(neighbour) + "\n") 
                # """
                self.environment.remove_agent(neighbour)
                self.environment.move_agent(self, movX, movY)
                self.lifeCounter = 0
                self.moved = True

                return True
        return False

    def lay_egg(self, posX, posY):
        """  produce a Shark to the position posX, posY """
        # """if self.trace_file != None:
        #     self.trace_file.write('Shark position : ' + str(self.posX) +
        #                           ',' + str(self.posY) +
        #                           'lay egg at position : ' + str(posX) +
        #                           ',' + str(posY) + '\n')
        # """
        return Shark(self.environment, posX, posY, 
                     self.lifeTime, self.breedTime,
                     self.trace_file)
    
    def decide(self):
        """ decision process of the Shark """
        if not self.alive:
            return
        self.moved = False
        self.lifeCounter += 1
        lastX = self.posX
        lastY = self.posY
        # Mort
        if self.lifeCounter == self.lifeTime:
            self.environment.remove_agent(self)
            return
        
        if not self.eat():
            # s'il n'a pas manger il bouge
             self.moved = self.random_move()
             
        # Gestation 
        self.gestation(lastX, lastY)
