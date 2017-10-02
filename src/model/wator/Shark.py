# Shark.py

from model.wator.Animal import Animal
import random

class Shark(Animal):

    """ Constructeur du requin """
    def __init__(self, environment, pasX, pasY, posX, posY, lifeTime, breedTime, trace_file=None):
        Animal.__init__(self, environment, pasX, pasY, posX, posY, breedTime, trace_file)
        self.lifeTime = lifeTime
        self.lifeCounter = 0 # Si = lifeTime, alors il meurt
        self.color = 'black'

    def getColor(self):
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

        lastX = self.posX
        lastY = self.posY
        
        possiblesMov = [(-1, 0), (0, -1), (1, 0), (0, 1)]        
        random.shuffle(possiblesMov)

        """ Radar autours du requin pour détecter un poisson """
        for x, y in possiblesMov:
            movX, movY = self.environment.compute_new_position(
                self.posX, self.posY, x, y)
            
            neighbour = self.environment.get_agent(movX, movY)
            if type(neighbour) == Shark or neighbour == None:
                continue
            else:
                """ C'est un poisson, on le mange """
                """
                if self.trace_file != None:
                    self.trace_file.write("Shark : " + str(self.id) + " eat fish : " + str(neighbour) + "\n") 
                """
                self.environment.remove_agent(neighbour)
                # neighbour2 = self.environment.get_agent_direction(self.posX, self.posY, x, y)

                self.environment.move_agent2(self, movX, movY)
                self.lifeCounter = 0
                self.moved = True
                return True
        return False

    def lay_egg(self, posX, posY):
        """if self.trace_file != None:
            self.trace_file.write('Shark position : ' + str(self.posX) +
                                  ',' + str(self.posY) +
                                  'lay egg at position : ' + str(posX) +
                                  ',' + str(posY) + '\n')
        """
        return Shark(self.environment,random.randint(-1,1),
                     random.randint(-1,1),posX, posY, self.lifeTime, self.breedTime,
                     self.trace_file)
    
    """ Décision """
    def decide(self):
        self.moved = False
        self.lifeCounter += 1
        lastX = self.posX
        lastY = self.posY

        """ Mort """
        if self.lifeCounter == self.lifeTime:
            self.environment.remove_agent(self)
            return
        
        if not self.eat():
            # s'il n'a pas manger il bouge
             self.moved = self.random_move()
             
        self.gestation(lastX, lastY)
            

        """ Gestation """
        
