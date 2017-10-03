# Particule.py

from model.core.Agent import Agent

class Particule(Agent):

    def __init__(self, environment, pasX, pasY, posX, posY, trace_file=None):
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.pasX = pasX
        self.pasY = pasY

    """ On laisse l'agent faire un move """
    def decide(self):
         move_x, move_y = self.environment.compute_new_position(self.posX,
                          self.posY, self.pasX, self.pasY)

         """
         Regarde si dans la direction, il a une colision
         """
         self.ticks += 1
         can_move = self.environment.can_move(move_x, move_y)

         """
         Si il peut avancer, il avance
         """
         if (can_move):
             self.environment.move_agent(self, move_x, move_y)
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
         move_x, move_y = self.environment.compute_new_position(self.posX,
                          self.posY, self.pasX, self.pasY)

         trace_string += ";" + str(self.pasX) + ";" + str(self.pasY) + "\n"

         can_move = self.environment.can_move(move_x, move_y)

         if self.trace_file != None:
             self.trace_file.write(trace_string)
         """
         Si il peut avancer, il avance
         """
         if (can_move):
             self.environment.move_agent(self, move_x, move_y)
             return

         return
