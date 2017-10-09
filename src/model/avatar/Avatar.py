# Avatar.py

from model.core.Agent import Agent
from model.avatar.AvatarControls import Controls
from collections import deque

class Avatar(Agent):

    def __init__(self, environment, posX, posY, tick, trace_file=None):
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.color = 'red'
        self.next_controls = deque([])
        self.move = Controls.UP
        self.tick = tick
        self.cpt = 1

    def decide(self):
        if self.cpt%self.tick == 0:
            self.cpt = 1

            if len(self.next_controls):
                self.move = self.next_controls.popleft()

            x = 0
            y = 0
            if self.move == Controls.RIGHT:
                x = 1
            elif self.move == Controls.LEFT:
                x = -1
            elif self.move == Controls.UP:
                y = -1
            elif self.move == Controls.DOWN:
                y = 1

            newX = 0
            newY = 0
            newX, newY = self.environment.compute_new_position(self.posX, self.posY, x, y)
            if self.environment.can_move(newX, newY):
                self.environment.move_agent(self, newX, newY)

            self.environment.update_target()

        self.cpt += 1
        return

    def new_move(self, move):
        self.next_controls.append(move)
