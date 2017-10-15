# Animal.py
from model.core.Agent import Agent

class Animal(Agent):
    """ Abstract class, represent an agent wich can produce other agent of same type

    the agent produce an other agent with a given period
    """

    
    def __init__(self, environment, posX, posY, breedTime, trace_file=None):
        """
        initialize the Agent, and the pregnancy period
        """
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.breedTime = breedTime
        self.breedCounter = 0
        self.moved = False
        self.baby = True

    def lay_egg(self, posX, posY):
        """
        produce an agent to the position posX, posY
        """
        return None
        
    def gestation(self, posX, posY):
        """ produce an other agent if the pregnancy period """
        self.breedCounter += 1
        if self.breedCounter == self.breedTime:
            self.breedCounter = 0
            if self.moved:
                self.environment.put_agent(self.lay_egg(posX, posY))
