import random
from model.Agent import Agent

class SMA:

    """
    Initialise un SMA avec nb_agent agent
    Chaque agent est positioné à une position aléatoire dans l'environement
    """
    def __init__(self, nb_agent, environment):
        random.seed()
        self.agents = []
        self.environment = environment

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

    def run():
        for agent in self.agents:
            agent.decide()
        print(self.environment)
