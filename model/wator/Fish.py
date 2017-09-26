# Fish.py

from core.Agent import Agent

class Fish(Agent):
    def __init__(self, id, environment, pasX, pasY, posX, posY, fishBreedTime, trace_file=None):
        Agent.__init__(self, id, environment, pasX, pasY, posX, posY, trace_file)
