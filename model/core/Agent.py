# Agent.py

next_id = 1

class Agent:

    def __init__(self, environment, pasX, pasY, posX, posY, trace_file=None):
        global next_id
        self.id = next_id 
        next_id += 1
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

    def decide(self):
        return
