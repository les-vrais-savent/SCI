# Agent.py

class Agent:

    def __init__(self, id, environment, pasX, pasY, posX, posY, trace_file=None):
        self.id = id
        self.color = 'blue'
        self.environment = environment
        self.pasX = pasX
        self.pasY = pasY
        self.posX = posX
        self.posY = posY
        self.trace_file = trace_file
        self.ticks = 0;
    def __str__(self):
        return str(self.id)

    """ On laisse l'agent faire un move """
    def decide(self):
         """
         Regarde si dans la direction, il a une colision
         """
         self.ticks += 1
         can_move = self.environment.can_move(self.posX, self.posY, self.pasX, self.pasY)

         """
         Si il peut avancer, il avance
         """
         if (can_move):
             self.posX, self.posY = self.environment.move_agent(self.posX, self.posY, self.pasX, self.pasY)
             return

         """
         Sinon, il change sa direction, et regarde s'il peut bouger
         à nouveau
         """
         self.color = 'red'
         trace_string = "agent;" + str(self.id) + ";"
         trace_string += str(self.ticks - 1) + ";" + str(self.posX)
         trace_string += ";" + str(self.posY) + ";" + str(self.pasX)
         trace_string += ";" + str(self.pasY)
         
         self.pasX = -self.pasX
         self.pasY = -self.pasY


         trace_string += ";" + str(self.pasX) + ";" + str(self.pasY) + "\n"

         can_move = self.environment.can_move(self.posX, self.posY, self.pasX, self.pasY)

         if self.trace_file != None:
             self.trace_file.write(trace_string)
         """
         Si il peut avancer, il avance
         """
         if (can_move):
             self.posX, self.posY = self.environment.move_agent(self.posX, self.posY, self.pasX, self.pasY)
             return

         return
