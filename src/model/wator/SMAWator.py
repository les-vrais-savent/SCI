import random
import time

from view.View import View
from model.wator.Shark import Shark 
from model.wator.Fish import Fish
from model.core.SMA import SMA

class SMAWator(SMA):
    """
    Special SMA class which initialize environement with fish and shark agent
    """

    
    def __init__(self, config, environment, view, configWator, trace_file=None):
        """ initialize the environment

        create and put all the agent on the environement

        :param config: dictionary which contains configuration parameters for the SMA class
        :param environement: pointer to the environment
        :param view: pointer to the view
        :param configWator: dictionary which contains configuration parameters for the wator simulation
        :param trace_file: file to write the log information (default = None)
        """
        SMA.__init__(self, config, environment, view, trace_file)

        # générer les coord initial de l'agent
        coord = [(x,y) for x in range(environment.sizeX)
                 for y in range (environment.sizeY)]
        random.shuffle(coord, random.random)
 
        for i in range(configWator['nb_shark']):
            x,y = coord.pop()
            environment.put_agent(
                Shark(environment,
                      x, y,
                      configWator['shark_life_time'],
                      configWator['shark_breed_time'],
                      self.trace_file))

        for i in range(configWator['nb_fish']):
            x,y = coord.pop()
            environment.put_agent(
                Fish(environment, x, y, 
                     configWator['shark_breed_time'],
                     self.trace_file))

    def count(self):
        """
        count the number of shark and fish agent on the environment

        :return: a tuple (number of fish, number of shark) present on the environment
        """
        nb_fish = 0
        nb_shark = 0

        x_max = self.environment.sizeX
        y_max = self.environment.sizeY

        for x in range(x_max):
            for y in range(y_max):
                ag = self.environment.get_agent(x,y)
                if type(ag) == Fish:
                    nb_fish += 1
                elif type(ag) == Shark:
                    nb_shark += 1
        return nb_fish, nb_shark

    def run(self):
        """ run a turn of the simulation and write on the tracefile the number of fish and shark alive """
        SMA.run(self)
        if self.trace_file != None:
            nb_fish, nb_shark = self.count()
            self.trace_file.write(str(self.ticks) + " " + str(nb_fish) + " " + str(nb_shark) + " " + str(nb_fish/(nb_shark + 0.001)) + "\n")
