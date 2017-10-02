# Animal.py
from model.core.Agent import Agent

class Animal(Agent):
        def __init__(self, environment, pasX, pasY, posX, posY, breedTime, trace_file=None):
            Agent.__init__(self, environment, pasX, pasY, posX, posY, trace_file)
            self.breedTime = breedTime
            self.breedCounter = 0
            self.moved = False
            self.baby = True

        def lay_egg(self, posX, posY):
            return None
            
        def gestation(self, posX, posY):
            self.breedCounter += 1

            if self.breedCounter == self.breedTime:
                self.breedCounter = 0
                if self.moved:
                    self.environment.put_agent(self.lay_egg(posX, posY))
