# EnvironmentAvatar.py

from model.core.Environment import Environment
from model.avatar.Avatar import Avatar
from model.avatar.Wall import Wall 
from model.avatar.Hunter import Hunter 
import sys

class EnvironmentAvatar(Environment):
    def __init__(self, sizeX, sizeY, torus, color='black'):
        Environment.__init__(self, sizeX, sizeY, torus, color)
        self.reverse = True
        self.gridDJ = [[(10000000000, self.reverse) for _ in range(sizeX)] for _ in range(sizeY)]
        self.avatar = Avatar(self, 0, 0)
        self.compute_dijkstra()

    def update_target(self):
        self.compute_dijkstra()

    def put_agent(self, agent):
        Environment.put_agent(self, agent)
        if isinstance(agent, Avatar):
            self.avatar = agent

    def get_next_position(self, agent):
        possibles_moves = [(1,0), (0, 1), (-1, 0), (0, -1)]

        min_move = None
        min_length = 1000000000
        for pasX, pasY in possibles_moves:
            x = agent.posX + pasX
            y = agent.posY + pasY
            if self.is_in(x, y) and self.hunter_can_move(x, y):
                (distance, _) = self.gridDJ[x][y]
                if distance < min_length:
                    min_length = distance
                    min_move = (x, y)
        return min_move
 
    def hunter_can_move(self, posX, posY):
        return not isinstance(self.get_agent(posX, posY), Wall) and not isinstance(self.get_agent(posX, posY), Hunter) 

    def compute_dijkstra(self):
        possibles_moves = [(1,0), (0, 1), (-1, 0), (0, -1)]
        self.reverse = not self.reverse
        super_set = set()
        current_val = 0
        super_set.add((self.avatar.posX, self.avatar.posY))
        while len(super_set) > 0:
            new_set = set()
            # On cherche toutes les positions aux alentours
            for s in super_set:
                for move in possibles_moves:
                    nextX = s[0]+move[0]
                    nextY = s[1]+move[1]
                    if self.is_in(nextX, nextY) and not (self.gridDJ[nextX][nextY][1] == self.reverse) and not isinstance(self.grid[nextX][nextY], Wall):
                        new_set.add((nextX, nextY))

            for s in super_set:
                self.gridDJ[s[0]][s[1]] = (current_val, self.reverse)
            
            super_set = new_set
            current_val += 1

    def display_dijkstra_value(self):
        env_str = "--------------------\n"
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                 env_str += str(self.gridDJ[x][y][0]) + "|"
            env_str += '\n'
        env_str += '--------------------\n'
        return env_str
