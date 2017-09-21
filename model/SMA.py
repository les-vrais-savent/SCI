import random
import time
from model.Agent import Agent
from view.View import View

class SMA:

    """
    Initialise un SMA avec nb_agent agent
    Chaque agent est positioné à une position aléatoire dans l'environement
    """
    def __init__(self, nb_agent, environment, view, delay, sheduling):

        self.sheduling = sheduling
        self.delay = delay
        self.agents = []
        self.environment = environment
        self.view = view

        
        
        # générer les coord initial de l'agent
        coord = [(x,y) for x in range(environment.size)
                 for y in range (environment.size)]
        random.shuffle(coord, random.random)
        
        for i in range(nb_agent):
            x,y = coord.pop()

            new_agent = Agent(i, environment,
                              random.randint(-1,1),
                              random.randint(-1,1),
                              x, y)
            environment.put_agent(new_agent)
            self.agents.append(new_agent)

    def run(self):

        if self.sheduling == "equitable":
            for agent in self.agents:
                agent.decide()
        self.view.update() 
        time.sleep(self.delay)
