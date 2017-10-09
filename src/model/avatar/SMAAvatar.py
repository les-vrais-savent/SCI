import random
import time

from view.View import View
from model.avatar.Avatar import Avatar
from model.avatar.Bonus import Bonus
from model.avatar.Wall import Wall 
from model.avatar.Hunter import Hunter 
from model.core.SMA import SMA
from model.avatar.AvatarControls import AvatarControls

class SMAAvatar(SMA):

    def __init__(self, config, environment, view, configAvatar, trace_file=None, ss=False):
        SMA.__init__(self, config, environment, view, trace_file)
        self.bonus_frequency = configAvatar['bonus_frequency']
        self.cpt_bonus = configAvatar['nb_bonus']
        self.gameEnd = False
        if ss:
            environment.reverse_hunter = False
            x = environment.sizeX // 2
            y = environment.sizeY // 2
      
            avatar = Avatar(environment,x , y, configAvatar['speed_avatar'], 0, self.trace_file)
            self.cont = AvatarControls(view, avatar)
            environment.put_agent(avatar)

            for x in [0, (environment.sizeX - 1)]:
                for y in range(environment.sizeY):
                    environment.put_agent(Hunter(environment, x, y, 100, self.trace_file))

            for y in [0, (environment.sizeX - 1)]:
                for x in range(environment.sizeX):
                    try:
                        environment.put_agent(Hunter(environment, x, y, 100, self.trace_file))
                    except ValueError:
                        continue
            return
        
        
        # générer les coord initial de l'agent
        coord = [(x,y) for x in range(environment.sizeX)
                 for y in range (environment.sizeY)]
        random.shuffle(coord, random.random)
 
        x,y = coord.pop()
        avatar = Avatar(environment, x, y, configAvatar['speed_avatar'], configAvatar['time_bonus'], configAvatar['nb_bonus'], self.trace_file)
        self.cont = AvatarControls(view, avatar)
        environment.put_agent(avatar)

        for i in range(configAvatar['nb_walls']):
            x,y = coord.pop()
            environment.put_agent(Wall(environment, x, y, self.trace_file))

        for i in range(configAvatar['nb_hunters']):
            x,y = coord.pop()
            environment.put_agent(Hunter(environment, x, y, configAvatar['speed_hunters'], self.trace_file))



    """
    Run qui renvoie True si la partie est terminé
    """
    def run(self):


        if ((self.ticks + 1) % self.bonus_frequency) == 0 and self.cpt_bonus != 0:
            coord = [(x,y) for x in range(self.environment.sizeX)
                     for y in range (self.environment.sizeY)]
            random.shuffle(coord, random.random)
            x,y = coord.pop()
            while(self.environment.get_agent(x, y) != None):
                x,y = coord.pop()
            self.environment.put_agent(Bonus(self.environment, x, y, self.trace_file))
            self.cpt_bonus -= 1
        
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
