import random
import time

from model.Agent import Agent
from view.View import View

class SMA:

    """
    Initialise un SMA avec nb_agent agent
    Chaque agent est positioné à une position aléatoire dans l'environement
    """
    def __init__(self, config, environment, view, trace_file=None):

        self.sheduling = config['sheduling']
        self.delay = config['delay']
        self.agents = []
        self.environment = environment
        self.view = view
        self.trace_file = trace_file
        self.ticks = 0;

        # générer les coord initial de l'agent
        coord = [(x,y) for x in range(environment.sizeX)
                 for y in range (environment.sizeY)]
        random.shuffle(coord, random.random)
        
        for i in range(config['nb_particles']):
            x,y = coord.pop()

            new_agent = Agent(i, environment,
                              random.randint(-1,1),
                              random.randint(-1,1),
                              x, y, self.trace_file)
            environment.put_agent(new_agent)
            self.agents.append(new_agent)

    def run(self):
        self.ticks += 1
        
        if self.sheduling == "equitable":
            for agent in self.agents:
                agent.decide()
        if self.view != None:
            self.view.update()
        if self.trace_file != None:
            self.trace_file.write("ticks;" + str(self.ticks) + "\n")
        if self.view != None:
            time.sleep(self.delay)
