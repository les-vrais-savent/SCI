# Environment.py

class Environment:
    """ Environment where the agents are placed
    
    composed by a matrix which represent the world (can be torus or not) and a list of all the agents 
    provide function to move agent on the matrix, to give information on the environment and manage agents
    """

    
    def __init__(self, sizeX, sizeY, torus, color='white'):
        """ initialize the environment

        initialize the environment variables and create the matrix represanting the world with the dimensions given in parameters

        :param sizeX: width of the matrix
        :param sizeY: length of the matrix
        :param torus: say if the world is torus or not
        :param color: color of the environment on the view (default: white)

        :type sizeX: int
        :type sizeY: int
        :type torus: bool
        :type color: str
        """
        self.torus = torus
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = [[None for _ in range(sizeX)] for _ in range(sizeY)]
        self.agents = []
        self.count = 0
        self.color = color


    def put_agent(self, agent):
        """ add an agent on the environment
        
            add an agent on the enviroment and put in on the matrix to its coordinates. (agent contains coordinates infromations)

            :param agent: the agent wich have to be put on the environment
            :type agent: model.core.Agent.Agent
            :raise: ValueError if an agent is already present where the new agent must to be
        """
        if self.grid[agent.posX][agent.posY] == None:
            self.grid[agent.posX][agent.posY] = agent
            self.agents.append(agent)
        else:
            raise ValueError('Agent Already present at this position')


    def remove_agent(self, agent):
        """ delete an agent from the environment
        
        delete the agent of the matrix and set its state to dead
        :param agent: the agent wich have to be deleted
        :type agent: model.core.Agent.Agent
        
        """
        self.grid[agent.posX][agent.posY] = None
        agent.alive = False


    def update_agents(self):
        """ Delete all dead agents from the agent list

        run through the agent list and remove all agent wich state is dead
        """
        new_agents = []
        for agent in self.agents:
            if agent.alive:
                new_agents.append(agent)
        self.agents = new_agents


    def compute_new_position(self, posX, posY, pasX, pasY):
        """ compute the new position given the current position and the direction
        
        compute the right position even if the world is torus

        :param posX: abscissa
        :param posY: ordinate
        :param pasX: value added to abscissa to compute new abscissa
        :param pasY: value added to ordinate to compute new ordinate
        """
        newX = posX+pasX 
        newY = posY+pasY
        
        if self.torus:
            newX = newX % self.sizeX
            newY = newY % self.sizeY

        return newX, newY


    def get_agent(self, x, y):
        """ return the agent at the coordinate (x,y)

        :param x: abscissa
        :param y: ordinate
        :return: None if no agent is present or the agent present
        """
        return self.grid[x][y]



    def can_move(self, posX, posY):
        """ look in the matrix if an obstacle is present at the coordinates given
        :param x: abscissa
        :param y: ordinate
        :return: False if an agent is present of (if the world is not torus) if the position is out of the world. True otherwise
        """
        # Si il y a un mur
        if (not self.torus and (posX < 0 or posX > self.sizeX-1 or posY < 0 or posY > self.sizeY-1)):
            return False

        # Si il y a un agent
        return self.get_agent(posX, posY) == None


    def is_in(self, posX, posY):
        """ look if the position is in the matrix
            
        :param posX: abscissa
        :param posY: ordinate
        :return: True if the position given is in the matrix, False otherwise
        """
       # Si on est hors plateau
        if (posX < 0 or posX > self.sizeX-1 or posY < 0 or posY > self.sizeY-1):
            return False
        return True


    def move_agent(self, agent, posX, posY):
        """ move the agent on the given coordinates

        if an agent is already present at its position, it is deleted

        :param agent: agent w
        :param posX: abscissa
        :param posY: ordinate
        """

        if self.grid[posX][posY] != None:
            self.grid[posX][posY].alive = False

        self.grid[posX][posY] = self.grid[agent.posX][agent.posY]
        self.grid[agent.posX][agent.posY] = None
        agent.posX = posX
        agent.posY = posY
        return posX, posY


    def __str__(self):
        """  the string representation of the environment

        :return:  the string representation of the environment
        """
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
