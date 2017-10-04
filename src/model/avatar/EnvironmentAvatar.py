# EnvironmentAvatar.py

from model.core.Environment import Environment
from model.avatar.Avatar import Avatar

class EnvironmentAvatar(Environment):
    def __init__(self, sizeX, sizeY, torus, color='white'):
        Environment.__init__(self, sizeX, sizeY, torus, color)
        self.gridDijkstra = [[None for _ in range(sizeX)] for _ in range(sizeY)]
        self.avatar = Avatar(self, 0, 0)

    def update_target(self):
        self.compute_dijkstra()

    def put_agent(self, agent):
        Environment.put_agent(self, agent)
        if isinstance(agent, Avatar):
            self.avatar = agent

    def get_next_position(self, agent):
        return

    def compute_dijkstra(self):
        possibles_moves = [(1,0), (0, 1), (-1, 0), (0, -1)]
        self.gridDijkstra[self.avatar.posX][self.avatar.posY] = 0
