import random
import time

from view.View import View
from model.avatar.Avatar import Avatar
from model.avatar.Wall import Wall 
from model.core.SMA import SMA
from model.avatar.AvatarControls import AvatarControls

class SMAAvatar(SMA):

    def __init__(self, config, environment, view, configAvatar, trace_file=None):
        SMA.__init__(self, config, environment, view, trace_file)

        # générer les coord initial de l'agent
        coord = [(x,y) for x in range(environment.sizeX)
                 for y in range (environment.sizeY)]
        random.shuffle(coord, random.random)
 
        x,y = coord.pop()
        avatar = Avatar(environment, x, y, self.trace_file)
        self.cont = AvatarControls(view, avatar)
        environment.put_agent(avatar)

        for i in range(configAvatar['nb_walls']):
            x,y = coord.pop()
            environment.put_agent(Wall(environment, x, y, self.trace_file))
