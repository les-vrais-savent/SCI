# Environment.py

class Environment:
    def __init__(self, sizeX, sizeY, torus):
        self.torus = torus
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = [[None for _ in range(sizeX)] for _ in range(sizeY)]
        # self.agents = [None for _ in range(sizeX * sizeY)]
        # self.agents_id = [i for i in range(0, sizeX * sizeY)]
        self.count = 0
    """
    ajoute un agent
    """
    def put_agent(self, agent):
        if self.grid[agent.posX][agent.posY] == None:
            self.grid[agent.posX][agent.posY] = agent
            # agent.id = self.agents_id.pop()
            # self.agents[agent.id] = agent
            # self.agents.append(agent)
        else:
            raise ValueError('Agent Already present at this position')

    """
    Suppression d'un agent 
    """
    def remove_agent(self, agent):
        self.grid[agent.posX][agent.posY] = None
        # self.agents[agent.id] = None
        # self.agents_id.append(agent.id)
        # for i in range(len(self.agents)):
        #     if self.agents[i].id == agent.id:
        #         self.agents.pop(i)
        #         break

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
        # if(x < self.sizeX and y < self.sizeY):
        return self.grid[x][y]
        # else:
        #     return None

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


    def can_move2(self, posX, posY):
        """ Si il y a un mur """
        if (not self.torus and (posX < 0 or posX > self.sizeX-1 or posY < 0 or posY > self.sizeY-1)):
            return False

        """ Si il y a un agent """
        return self.get_agent(posX, posY) == None

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
    déplace l'agent a la case demandé sans vérification
    """
    def move_agent2(self, agent, posX, posY):
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
