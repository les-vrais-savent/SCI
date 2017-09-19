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

        environment.put_agent(self)

    """ On laisse l'agent faire un move """
    def decide(self):
         """
         Demande à l'environnement qui sont ses voisins
         Regarde si dans la direction, il a une colision
           Si pas de coli, il avance
           Si coli, il calcul sa nouvelle direction, et avance
         """
           

         return
