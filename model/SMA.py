import random
from model.Agent import Agent

class SMA:

    """
    Initialise un SMA avec nb_agent agent
    Chaque agent est positioné à une position aléatoire dans l'environement
    """
    def __init__(self, nb_agent, environement):
        random.seed()
        self.agents = []
        self.environement = environement

        # générer les coord initial de l'agent
        coord = [(x,y) for x in range(environement.size)
                 for y in range (environement.size)]
        random.shuffle(coord, random.random)
        
        for i in range(nb_agent):
            x,y = coord.pop()

            new_agent = Agent(i, environement,
                              x + random.randint(-1,1),
                              y + random.randint(-1,1),
                              x, y)
            environement.put_agent(new_agent)
            self.agents.append(new_agent)

    def run():
        for agent in self.agents:
            agent.decide()


