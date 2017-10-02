import random
import time

from view.View import View
from model.wator.Shark import Shark 
from model.wator.Fish import Fish
from model.core.SMA import SMA

class SMAWator(SMA):

    def __init__(self, config, environment, view, configWator, trace_file=None):

        SMA.__init__(self, config, environment, view, trace_file)

        # générer les coord initial de l'agent
        coord = [(x,y) for x in range(environment.sizeX)
                 for y in range (environment.sizeY)]
        random.shuffle(coord, random.random)
 
        for i in range(configWator['nb_shark']):
            x,y = coord.pop()
            environment.put_agent(
                Shark(environment,
                      random.randint(-1, 1),
                      random.randint(-1, 1), x, y,
                      configWator['shark_life_time'],
                      configWator['shark_breed_time'],
                      self.trace_file))

        for i in range(configWator['nb_fish']):
            x,y = coord.pop()
            environment.put_agent(
                Fish(environment, random.randint(-1,1),
                     random.randint(-1,1),
                     x, y, configWator['shark_breed_time'],
                     self.trace_file))

