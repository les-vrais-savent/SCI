# EnvironmentAvatar.py

from model.core.Environment import Environment
from model.avatar.Avatar import Avatar

class EnvironmentAvatar(Environment):
    def __init__(self, sizeX, sizeY, torus, color='white'):
        Environment.__init__(self, sizeX, sizeY, torus, color)
        self.reverse = True
        self.gridDJ = [[(-1, self.reverse) for _ in range(sizeX)] for _ in range(sizeY)]
        self.avatar = Avatar(self, 0, 0)

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
        for i in range(4):
            pasX, pasY = possibles_moves[i]
            x = agent.posX + pasX
            y = agent.posY + pasY
            (distance, _) = self.gridDJ[x][y]
            if distance < min_length:
                min_length = distance
                min_move = possibles_moves[i]
        return min_move
        
        
        return 


    def dijkstra_recursion(self, posX, posY, val):
        self.gridDJ[self.avatar.posX][self.avatar.posY] = (val, self.reverse)
        possibles_moves = [(1,0), (0, 1), (-1, 0), (0, -1)]
        for move in possibles_moves:
            nextX = posX+move[0]
            nextY = posY+move[1]
            if self.environment.is_in(nextX, nextY):
                if self.gridDJ[nextX][nextY][1] == self.reverse:
                    dijkstra_recursion(nextX, nextY, val+1) 
                

    def compute_dijkstra(self):
        self.reverse = not self.reverse
        dijkstra_recursion(self.avatar.posX, self.avatar.posY, 0)

    def display_dijkstra_value(self):
        env_str = "--------------------\n"
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                 env_str += str(self.grid[x][y][0]) + "|"
            env_str += '\n'
        env_str += '--------------------\n'
        return env_str
 
