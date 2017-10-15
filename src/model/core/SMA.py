import random
import time

from model.core.Agent import Agent
from view.View import View

from model.particules.Particule import Particule

class SMA:
    """ main class for the multi agent system
    
    used to manage agent and update the view
    """

    def __init__(self, config, environment, view, trace_file=None):
        """ initialize the environment

        create and put all the agent on the environement

        :param config: dictionary which contains configuration parameters
        :param environement: pointer to the environment
        :param view: pointer to the view
        :trace_file: file to write the log information (default = None)
        """
        
        self.sheduling = config['sheduling']
        self.delay = config['delay']
        self.environment = environment
        self.view = view
        self.trace_file = trace_file
        self.ticks = 0;

    def run(self):
        """ run a round of decision and update the view

        agents are taken (the order depend of the sheduling mode) and make a decision. after that, the view is update
        """
        self.ticks += 1
        # On reprend tous les agents

        if self.sheduling == "sequentiel":
            for ag in self.environment.agents:
                ag.decide()

        elif self.sheduling == "equitable":
            ids = [x for x in range(len(self.environment.agents)-1)]
            random.shuffle(ids)
            for id_agent in ids:
                self.environment.agents[id_agent].decide()

        elif self.sheduling == "aleatoire":
            for _ in range(len(agents)):
                nb_alea = random.randint(0, len(agents)-1)
                self.environment.agents[nb_alea].decide() 

        if self.view != None:
            self.view.update()
        #if self.trace_file != None:
            #self.trace_file.write("ticks;" + str(self.ticks) + "\n")
        if self.view != None:
            time.sleep(self.delay)

        self.environment.update_agents()
