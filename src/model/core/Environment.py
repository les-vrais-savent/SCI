# Environment.py

class Environment:
    def __init__(self, sizeX, sizeY, torus, color='white'):
        self.torus = torus
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = [[None for _ in range(sizeX)] for _ in range(sizeY)]
        self.count = 0
        self.color = color

    """
    ajoute un agent
    """
    def put_agent(self, agent):
        if self.grid[agent.posX][agent.posY] == None:
            self.grid[agent.posX][agent.posY] = agent
        else:
            raise ValueError('Agent Already present at this position')

    """
    Suppression d'un agent 
    """
    def remove_agent(self, agent):
        self.grid[agent.posX][agent.posY] = None
        agent.alive = False

    """
    Calcul de la nouvelle position selon torus
    """
    def compute_new_position(self, posX, posY, pasX, pasY):
        newX = posX+pasX 
        newY = posY+pasY
        
        if self.torus:
            newX = newX % self.sizeX
            newY = newY % self.sizeY

        return newX, newY

    """
    renvois l'agent présent à la position (x,y)
    """
    def get_agent(self, x, y):
        return self.grid[x][y]

    """
    renvois l'agent présent à la position (x,y)
    """
    def get_agent_direction(self, posX, posY, pasX, pasY):
        x,y = self.compute_new_position(posX, posY, pasX, pasY)
        if(x < self.sizeX and y < self.sizeY):
            return self.grid[x][y]
        else:
            return None

    """
    Vérifie la présence d'un obstacle
    """
    def can_move(self, posX, posY):
        """ Si il y a un mur """
        if (not self.torus and (posX < 0 or posX > self.sizeX-1 or posY < 0 or posY > self.sizeY-1)):
            return False

        """ Si il y a un agent """
        return self.get_agent(posX, posY) == None

    """
    déplace l'agent a la case demandé sans vérification
    """
    def move_agent(self, agent, posX, posY):
        self.grid[posX][posY] = self.grid[agent.posX][agent.posY]
        self.grid[agent.posX][agent.posY] = None
        agent.posX = posX
        agent.posY = posY
        return posX, posY

    """
    Affiche l'environnement 
    """
    def __str__(self):
        env_str = "--------------------\n"
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                 if (self.grid[x][y] == None):
                     env_str += " |"
                 else:
                     env_str += str(self.grid[x][y]) + "|"
            env_str += '\n'
        env_str += '--------------------\n'
        return env_str
