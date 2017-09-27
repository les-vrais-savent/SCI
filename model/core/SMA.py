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
        self.agents = []
        self.environment = environment
        self.view = view
        self.trace_file = trace_file
        self.ticks = 0;

    def run(self):
        self.ticks += 1

        if self.sheduling == "sequentiel":
            for agent in self.agents:
                agent.decide()
        elif self.sheduling == "equitable":
            equi = self.agents
            random.shuffle(equi)
            for agent in equi:
                agent.decide()
        elif self.sheduling == "aleatoire":
            for _ in range(len(self.agents)):
                nb_alea = random.randint(0, len(self.agents)-1)
                self.agents[nb_alea].decide() 

        if self.view != None:
            self.view.update()
        if self.trace_file != None:
            self.trace_file.write("ticks;" + str(self.ticks) + "\n")
        if self.view != None:
            time.sleep(self.delay)
