# AvatarControls.py

from enum import Enum

class Controls(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

class AvatarControls():

    def __init__(self, view, avatar):
        self.view = view
        self.avatar = avatar
        """
        Définit les contrôles possibles
        """
        self.view.window.bind('<Left>', lambda event, c=Controls.LEFT: self.avatar.new_move(c))
        self.view.window.bind('<Right>', lambda event, c=Controls.RIGHT: self.avatar.new_move(c))
        self.view.window.bind('<Up>', lambda event, c=Controls.UP: self.avatar.new_move(c))
        self.view.window.bind('<Down>', lambda event, c=Controls.DOWN: self.avatar.new_move(c))

        return
