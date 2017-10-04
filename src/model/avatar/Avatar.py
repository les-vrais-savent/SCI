# Avatar.py

from model.core.Agent import Agent
from model.avatar.AvatarControls import Controls
from collections import deque

class Avatar(Agent):

    def __init__(self, environment, posX, posY, trace_file=None):
        Agent.__init__(self, environment, posX, posY, trace_file)
        self.color = 'red'
        self.next_controls = deque([])

    def decide(self):
        x = 0
        y = 0
        if len(self.next_controls):
            move = self.next_controls.popleft()
            if move == Controls.RIGHT:
                x = 1
            elif move == Controls.LEFT:
                x = -1
            elif move == Controls.UP:
                y = -1
            elif move == Controls.DOWN:
                y = 1

            newX = 0
            newY = 0
            newX, newY = self.environment.compute_new_position(self.posX, self.posY, x, y)
            if self.environment.can_move(newX, newY):
                self.environment.move_agent(self, newX, newY)

        self.environment.update_target()
        return

    def new_move(self, move):
        self.next_controls.append(move)
