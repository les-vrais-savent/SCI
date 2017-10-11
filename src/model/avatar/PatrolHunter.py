from model.avatar.Hunter import Hunter
from model.core.Agent import Agent
import random

class PatrolHunter(Hunter):
        def __init__(self, environment, posX, posY, tick, trace_file=None):
            Hunter.__init__(self, environment, posX, posY, tick, trace_file)
            self.reverse = False
            self.init_color = 'yellow'
            self.gridDJ = [[(10000000000, self.reverse) for _ in range(environment.sizeX)] for _ in range(environment.sizeY)]

            self.goal = Agent(environment,
                              random.randint(0, environment.sizeX - 1),
                              random.randint(0, environment.sizeY - 1),
                              None)

            
        def move(self, move, distance):
            env = self.environment
            if distance > 10:
                self.reverse = not self.reverse
                env.compute_dijkstra(self.gridDJ, self.goal,
                                     self.reverse)
                
                
                move, _ = env.get_next_position(self.goal,
                                                self.gridDJ,
                                                env.reverse_hunter)

                if move != None:
                    self.simple_move(move)
                self.init_color= 'yellow'
                return False
            else:
                self.init_color= 'blue'
                return self.simple_move(move)
