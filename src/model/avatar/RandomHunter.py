from model.avatar.Hunter import Hunter

class RandomHunter(Hunter):
    """
    The agent RandomHunter

    Child of Hunter class, overide the move method to move randomly if the avatar is too far
    """

    
    def __init__(self, environment, posX, posY, tick, trace_file=None):
        Hunter.__init__(self, environment, posX, posY, tick, trace_file)
        self.init_color = 'deep sky blue'

    
    def move(self, move, distance):
        """ if the distance between the RandomHunter and the Avatar is highter than 10, move randomly and set its color to deep sky blue, otherwise, move like a Hunter and set its color to blue
        """
        if distance > 10:
            self.init_color= 'deep sky blue'
            self.random_move()
            return False
        else:
            self.init_color= 'blue'
            return self.simple_move(move)


