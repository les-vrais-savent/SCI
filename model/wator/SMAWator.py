import random
import time

from view.View import View
from model.wator.Shark import Shark 
from model.wator.Fish import Fish
from model.core.SMA import SMA

class SMAWator(SMA):

    def __init__(self, config, environment, view, trace_file=None):

        SMA.__init__(self, config, environment, view, trace_file)

        # générer les coord initial de l'agent
        coord = [(x,y) for x in range(environment.sizeX)
                 for y in range (environment.sizeY)]
        random.shuffle(coord, random.random)
 
        for i in range(config['nb_particles']):
            x,y = coord.pop()
            environment.put_agent(Fish(environment,
                                       random.randint(-1,1),
                                       random.randint(-1,1),
                                       x, y, 3, self.trace_file))
            if i%3 == 0: 
                x,y = coord.pop()
                environment.put_agent(Shark(environment,
                                            random.randint(-1, 1),
                                            random.randint(-1, 1),
                                            x, y, 5, 3, self.trace_file)) 
