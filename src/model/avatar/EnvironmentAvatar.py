# EnvironmentAvatar.py

from model.core.Environment import Environment
from model.avatar.Avatar import Avatar
from model.avatar.Wall import Wall 
from model.avatar.Hunter import Hunter 
import sys

class EnvironmentAvatar(Environment):
    def __init__(self, sizeX, sizeY, torus, color='black'):
        Environment.__init__(self, sizeX, sizeY, torus, color)
        self.reverse = False
        self.reverse_hunter = False
        self.gridDJ = [[(10000000000, self.reverse) for _ in range(sizeX)] for _ in range(sizeY)]
        self.avatar = Avatar(self, 0, 0, 0, 0, 0)
        
        self.compute_dijkstra(self.gridDJ, self.avatar, self.reverse)
        
        
    def update_target(self):
        self.reverse = not self.reverse
        self.compute_dijkstra(self.gridDJ, self.avatar, self.reverse)

    def put_agent(self, agent):
        Environment.put_agent(self, agent)
        if isinstance(agent, Avatar):
            self.avatar = agent

    def get_next_position(self, agent, grid, reverse=False):
        possibles_moves = [(1,0), (0, 1), (-1, 0), (0, -1)]

        def cmp(i,j):
            if reverse:
                return i > j
            return i < j

        move = None
        move_length = -1 if reverse else 100000000
        for pasX, pasY in possibles_moves:
            x, y = self.compute_new_position(agent.posX, agent.posY, pasX, pasY)
            if self.is_in(x, y) and self.hunter_can_move(x, y):
                (distance, _) = grid[x][y]
                if cmp(distance,move_length):
                    move_length = distance
                    move = (x, y)
        
        return (move,move_length)
 
    def hunter_can_move(self, posX, posY):
        return not isinstance(self.get_agent(posX, posY), Wall) and not isinstance(self.get_agent(posX, posY), Hunter) 

    def compute_dijkstra(self, grid, target, reverse):
        possibles_moves = [(1,0), (0, 1), (-1, 0), (0, -1)]
        # self.reverse = not self.reverse
        super_set = set()
        current_val = 0
        super_set.add((target.posX, target.posY))
        while len(super_set) > 0:
            new_set = set()
            # On cherche toutes les positions aux alentours
            for s in super_set:
                for move in possibles_moves:
                    nextX, nextY = self.compute_new_position(s[0], s[1], move[0], move[1])
                    if self.is_in(nextX, nextY) and not (self.gridDJ[nextX][nextY][1] == self.reverse) and not isinstance(self.grid[nextX][nextY], Wall):
                        new_set.add((nextX, nextY))

            for s in super_set:
                grid[s[0]][s[1]] = (current_val, self.reverse)

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
