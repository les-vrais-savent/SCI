from model.avatar.Wall import Wall 

class Bonus(Wall):

    def __init__(self, environment, posX, posY, trace_file=None):
        Wall.__init__(self, environment, posX, posY, trace_file)
        self.color = 'yellow'
        self.form = 'oval'
