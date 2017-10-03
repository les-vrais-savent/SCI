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
        self.agents = []

    def update_agents(self):
        self.agents = []
        for l in self.environment.grid:
            for agent in l:
                if agent != None:
                    self.agents.append(agent)

    def run(self):
        self.ticks += 1
        """ On reprend tous les agents """
        
        self.update_agents()

        if self.sheduling == "sequentiel":
            for ag in self.agents:
                ag.decide()

        elif self.sheduling == "equitable":
            # A corriger
            for l in self.environment.grid:
                for agent in l:
                    if agent != None:
                        agents.append(agent)

            random.shuffle(agents)
            for agent in agents:
                agent.decide()

        elif self.sheduling == "aleatoire":
            # A corriger
            for l in self.environment.grid:
                for agent in l:
                    if agent != None:
                        agents.append(agent)

            for _ in range(len(agents)):
                nb_alea = random.randint(0, len(agents)-1)
                agents[nb_alea].decide() 

        if self.view != None:
            self.view.update()
        #if self.trace_file != None:
            #self.trace_file.write("ticks;" + str(self.ticks) + "\n")
        if self.view != None:
            time.sleep(self.delay)
