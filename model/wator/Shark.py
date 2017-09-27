# Shark.py

from core.Agent import Agent

class Shark(Agent):
    def __init__(self, id, environment, pasX, pasY, posX, posY, lifeTime, trace_file=None):
        Agent.__init__(self, id, environment, pasX, pasY, posX, posY, trace_file)
        self.lifeTime = lifeTime

    def decide(self):
        
