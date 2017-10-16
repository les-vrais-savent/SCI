from model.avatar.Wall import Wall 

class Bonus(Wall):
    """
    A static agent. its color is yellow and its form is oval
    """
    def __init__(self, environment, posX, posY, trace_file=None):
        Wall.__init__(self, environment, posX, posY, trace_file)
        self.color = 'yellow'
        self.form = 'oval'
