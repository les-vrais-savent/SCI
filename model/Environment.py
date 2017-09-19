class Environment:
    def __init__(self, size):
        self.size = size
        self.grid = [[None] * size] * size

    """
    ajoute un agent à la position (x,y)
    """
    def put_agent(self, agent):
        self.grid[agent.posX][agent.posY] = agent

    """
    renvois l'agent présent à la position (x,y)
    """
    def get_agent(self, x, y):
        return self.grid[x][y]

    """
    Vérifie la présence d'un obstacle
    """
    def can_move(self, x, y):
        """ Si il y a un mur """
        if (x < 0 or x > size or y < 0 or y > size):
            return False

        """ Si il y a un agent """
        if (self.get_agent(x, y) != None):
            return False

        return True
 
    """
    déplace un agent de la position (x_src,y_src) vers la position (x_dest,y_dest)
    si la position final est déjà occupé, l'agent ne bouge pas 
    """
    def move_agent(self, x_src, y_src, x_dest, y_dest):
        if self.grid[x_dest][y_dest] != None:
            return
        self.grid[x_dest][y_dest] = self.grid[x_src][y_src]
        self.grid[x_src][y_src] = None
