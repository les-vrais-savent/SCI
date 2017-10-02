import random
import time

from model.core.Agent import Agent
from view.View import View

from model.particules.Particule import Particule

class SMA:

    """
    Initialise un SMA 
    """
    def __init__(self, config, environment, view, trace_file=None):

        self.sheduling = config['sheduling']
        self.delay = config['delay']
        self.environment = environment
        self.view = view
        self.trace_file = trace_file
        self.ticks = 0;

    def run(self):
        self.ticks += 1
        """ On reprend tous les agents """

        if self.sheduling == "sequentiel":
            for l in self.environment.grid:
                for agent in l:
                    if agent != None:
                        agent.decide()
        elif self.sheduling == "equitable":
            equi = self.environment.agents
            random.shuffle(equi)
            for agent in equi:
                if agent != None:
                    agent.decide()
        elif self.sheduling == "aleatoire":
            for _ in range(len(self.agents)):
                nb_alea = random.randint(0, len(self.agents)-1)
                agent = self.environment.agents[nb_alea]
                if agent != None:
                    agent.decide() 

        if self.view != None:
            self.view.update()
        if self.trace_file != None:
            self.trace_file.write("ticks;" + str(self.ticks) + "\n")
        if self.view != None:
            time.sleep(self.delay)
