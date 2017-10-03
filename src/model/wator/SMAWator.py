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
        SMA.run(self)
        if self.trace_file != None:
            nb_fish, nb_shark = self.count()
            self.trace_file.write(str(self.ticks) + " " + str(nb_fish) + " " + str(nb_shark) + "\n")
