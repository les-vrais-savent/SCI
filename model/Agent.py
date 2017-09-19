# Agent.py

class Agent:

    def __init__(self, id, environment, pasX, pasY, posX, posY):
        self.id = id
        self.color = 'blue'
        self.environment = environment
        self.pasX = pasX
        self.pasY = pasY
        self.posX = posX
        self.posY = posY

    def __str__(self):
        return str(self.id)

    """ On laisse l'agent faire un move """
    def decide(self):
         """
         Regarde si dans la direction, il a une colision
         """
         moveX = self.posX+self.pasX
         moveY = self.posY+self.pasY
         can_move = self.environment.can_move(moveX, moveY)

         """
         Si il peut avancer, il avance
         """
         if (can_move):
             self.environment.move_agent(self.posX, self.posY, moveX, moveY)
             self.posX = moveX
             self.posY = moveY
             return

         """
         Sinon, il change sa direction, et regarde s'il peut bouger
         à nouveau
         """
         self.pasX = -self.pasX
         self.pasY = -self.pasY

         moveX = self.posX+self.pasX
         moveY = self.posY+self.pasY 
         can_move = self.environment.can_move(moveX, moveY)

         """
         Si il peut avancer, il avance
         """
         if (can_move):
             self.environment.move_agent(self.posX, self.posY, moveX, moveY)
             self.posX = moveX
             self.posY = moveY
             return

         return
