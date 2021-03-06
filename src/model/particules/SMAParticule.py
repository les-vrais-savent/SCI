import random
import time

from model.core.Agent import Agent
from view.View import View

from model.particules.Particule import Particule
from model.core.SMA import SMA

class SMAParticule(SMA):
    """
    Special SMA class which initialize environement with particles
    """
    def __init__(self, config, environment, view, trace_file=None):
        """ initialize the environment

        create and put all the agent on the environement

        :param config: dictionary which contains configuration parameters
        :param environement: pointer to the environment
        :param view: pointer to the view
        :trace_file: file to write the log information (default = None)
        """
        SMA.__init__(self, config, environment, view, trace_file)
        # générer les coord initial de l'agent
        coord = [(x,y) for x in range(environment.sizeX)
                 for y in range (environment.sizeY)]
        random.shuffle(coord, random.random)
        
        for i in range(config['nb_particles']):
            x,y = coord.pop()

            new_agent = Particule(environment,
                                  random.randint(-1,1),
                                  random.randint(-1,1),
                                  x, y, self.trace_file)
            environment.put_agent(new_agent)
