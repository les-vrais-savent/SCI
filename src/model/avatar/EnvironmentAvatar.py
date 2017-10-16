# EnvironmentAvatar.py

from model.core.Environment import Environment
from model.avatar.Avatar import Avatar
from model.avatar.Wall import Wall 
from model.avatar.Hunter import Hunter 
import sys

class EnvironmentAvatar(Environment):
    """ Environement where the agents are placed

    provide function to help hunter to move, a distance matrix is mapped on the environmeent (one cell for each position on the environement), each cell contain the distance betwenn its position and the avatar  (computed with dijkstra algorithm)
    """


    
    def __init__(self, sizeX, sizeY, torus, color='black'):
        """ initialize the environment

        initialize the environment variables and create the matrix represanting the world with the dimensions given in parameters. Initialize data structure that compute the distance matrix

        :param sizeX: width of the matrix
        :param sizeY: length of the matrix
        :param torus: say if the world is torus or not
        :param color: color of the environment on the view (default: white)
        :type sizeX: int
        :type sizeY: int
        :type torus: bool
        :type color: str
        """
        Environment.__init__(self, sizeX, sizeY, torus, color)
        self.reverse = False
        self.reverse_hunter = False
        self.gridDJ = [[(10000000000, self.reverse) for _ in range(sizeX)] for _ in range(sizeY)]
        self.avatar = Avatar(self, 0, 0, 0, 0, 0)
        
        self.compute_dijkstra(self.gridDJ, self.avatar, self.reverse)
        
        
    def update_target(self):
        """ update the distance matrix """
        self.reverse = not self.reverse
        self.compute_dijkstra(self.gridDJ, self.avatar, self.reverse)

    def put_agent(self, agent):
        """ like Environment.put_agent but if the agent is the avatar, save it in a pointer """
        Environment.put_agent(self, agent)
        if isinstance(agent, Avatar):
            self.avatar = agent

    def get_next_position(self, agent, grid, reverse=False):
        """ return the position in the environement which bring the agent closer/further of the avatar

        :param agent: the agent which need to move
        :param grid: the distance matrix
        :param reverse: if True, chose the position that bring the agent closer of the avatar, if false, chose the position that bring the agent further of the avatar

        :return: (new_position, distance) where new_position is the coordinate where the agent has to move and distance is the distance between the agent and the avatar
        """
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
        """ say if a hunter can move on the given position

        :param posX: abscissa
        :param posY: ordinate
        
        :return: True if the current position don't contain a Wall or an other Hunter False otherwise (a Hunter can move to a position that contain the Avatar)
        """
        return not isinstance(self.get_agent(posX, posY), Wall) and not isinstance(self.get_agent(posX, posY), Hunter) 

    def compute_dijkstra(self, grid, target, reverse):
        """ compute the distance matrix """
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
        """ display the distance matrix """
        env_str = "--------------------\n"
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                 env_str += str(self.gridDJ[x][y][0]) + "|"
            env_str += '\n'
        env_str += '--------------------\n'
        return env_str
