# Agent.py
import random

next_id = 1

class Agent:
    """
    an Agent

    an agent have a position in the environement, contain a pointer to the environment and a traceFile to log information
    """
    def __init__(self, environment, posX, posY, trace_file=None):
        """ Initialize the Agent
        
        set its view representation (color, form)
  
        :param environment: pointer to the environment where the agent live
        :param posX: abscissa coordinate of the agent
        :param posY: ordinate coordinate of the agent
        :trace_file: file to write the log information (default = None)

        """
        global next_id
        self.id = next_id 
        next_id += 1
        self.color = 'blue'
        self.environment = environment
        self.posX = posX
        self.posY = posY
        self.trace_file = trace_file
        self.ticks = 0;
        self.alive = True
        self.form = 'oval'

    def __str__(self):
        """  the string representation of the agent

        :return:  the string representation of the agent
        """
        return str(self.id)

    def getColor(self):
        """  the color of the agent on the view

        :return: the color of the agent on the view
        """
        return self.color

    def random_move(self):
        """ try to move the agent in a random direction

        all the possible direction are tried (higth, low, right, left) if any direction is possible

        :return: True if the agent moved, False otherwise
        """
        possiblesMov = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        random.shuffle(possiblesMov)        
        
        for x, y in possiblesMov:
            movX, movY = self.environment.compute_new_position(
                self.posX, self.posY, x, y)
                        
            if self.environment.can_move(movX, movY):
                self.environment.move_agent(self, movX, movY)
                return True

        return False
    
    def decide(self):
        """ virtual method for the decision process of the agent """
        return
