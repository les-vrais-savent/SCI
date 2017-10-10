from model.avatar.Hunter import Hunter

class RandomHunter(Hunter):
        def __init__(self, environment, posX, posY, tick, trace_file=None):
            Hunter.__init__(self, environment, posX, posY, tick, trace_file)
            self.init_color = 'deep sky blue'

        def move(self, move, distance):
            if distance > 10:
                self.init_color= 'deep sky blue'
                self.random_move()
                return False
            else:
                self.init_color= 'blue'
                return self.simple_move(move)


