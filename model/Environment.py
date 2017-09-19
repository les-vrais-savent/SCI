class Environment:
    def __init__(self, size):
        self.size = size
        self.gird = [[None] * size] * size

    """
    ajoute un agent à la position (x,y)
    """
    def put_agent(self, agent, x, y):
        self.gird[x][y] = agent

    """
    renvois l'agent présent à la position (x,y)
    """
    def get_agent(self, x, y):
        return self.gird[x][y]
        
    """
    déplace un agent de la position (x_src,y_src) vers la position (x_dest,y_dest)
    si la position final est déjà occupé, l'agent déjà présent est supprimé de l'environement (mais pas du SMA)
    """
    def move_agent(self, x_src, y_src, x_dest, y_dest):
        self.gird[x_dest][y_dest] = self.gird[x_src][y_src]
        self.gird[x_src][y_src] = None


