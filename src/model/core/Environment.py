# Environment.py

class Environment:
    def __init__(self, sizeX, sizeY, torus):
        self.torus = torus
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = [[None for _ in range(sizeX)] for _ in range(sizeY)]
        self.agents = []

    """
    ajoute un agent
    """
    def put_agent(self, agent):
        if self.grid[agent.posX][agent.posY] == None:
            self.grid[agent.posX][agent.posY] = agent
            self.agents.append(agent)
        else:
            raise ValueError('Agent Already present at this position')

    """
    Suppression d'un agent 
    """
    def remove_agent(self, agent):
        self.grid[agent.posX][agent.posY] = None
        for i in range(len(self.agents)):
            if self.agents[i].id == agent.id:
                self.agents.pop(i)
                break

    """
    Calcul de la nouvelle position selon torus
    """
    def compute_new_position(self, posX, posY, pasX, pasY):
        newX = posX+pasX
        newY = posY+pasY

        if self.torus:
            if newX < 0:
                newX = self.sizeX-1
            elif newX > self.sizeX-1:
                newX = 0
 
            if newY < 0:
                newY = self.sizeY-1
            elif newY > self.sizeY-1:
                newY = 0

        return newX, newY

    """
    renvois l'agent présent à la position (x,y)
    """
    def get_agent(self, x, y):
        if(x < self.sizeX and y < self.sizeY):
            return self.grid[x][y]
        else:
            return None

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
    renvoi la liste des coordonées du voisinage de la case (posx,poxy)
    """
    # def neighborhood_coord(self, posX, posY):
    #     possiblesMov = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    #     return [self.compute_new_position(posX,posY, i, j)
    #             for (i,j) in possiblesMov]
    
    """
    Vérifie la présence d'un obstacle
    """
    def can_move(self, posX, posY, pasX, pasY):
        """ Si il y a un mur """
        moveX, moveY = self.compute_new_position(posX, posY, pasX, pasY)
        if (not self.torus and (moveX < 0 or moveX > self.sizeX-1 or moveY < 0 or moveY > self.sizeY-1)):
            return False

        """ Si il y a un agent """
        if (self.get_agent(moveX, moveY) != None):
            return False
        return True

    """
    déplace un agent
    si la position final est déjà occupé, l'agent ne bouge pas 
    """
    def move_agent(self, posX, posY, pasX, pasY):
        """ Si il ne peut pas bouger, il ne bouge pas """
        if not self.can_move(posX, posY, pasX, pasY):
            return posX, posY

        moveX, moveY = self.compute_new_position(posX, posY, pasX, pasY)

        self.grid[moveX][moveY] = self.grid[posX][posY]
        self.grid[posX][posY] = None

        return moveX, moveY

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
