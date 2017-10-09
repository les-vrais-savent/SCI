import random
import time

from view.View import View
from model.avatar.Avatar import Avatar
from model.avatar.Wall import Wall 
from model.avatar.Hunter import Hunter 
from model.core.SMA import SMA
from model.avatar.AvatarControls import AvatarControls

class SMAAvatar(SMA):

    def __init__(self, config, environment, view, configAvatar, trace_file=None):
        SMA.__init__(self, config, environment, view, trace_file)

        self.gameEnd = False

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

        for i in range(configAvatar['nb_hunters']):
            x,y = coord.pop()
            environment.put_agent(Hunter(environment, x, y, configAvatar['speed_hunters']/config['delay'], self.trace_file))

    """
    Run qui renvoie False si la partie est terminé
    """
    def run(self):
        if self.gameEnd:
            return True 

        self.ticks += 1
        """ On reprend tous les agents """

        for ag in self.environment.agents:
            if ag.decide():
                self.gameEnd = True
                break

        if self.view != None:
            self.view.update()
        #if self.trace_file != None:
            #self.trace_file.write("ticks;" + str(self.ticks) + "\n")
        if self.view != None:
            time.sleep(self.delay)

        self.environment.update_agents()

        return False
