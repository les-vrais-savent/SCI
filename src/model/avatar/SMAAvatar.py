import random
import time

from view.View import View
from model.avatar.Avatar import Avatar
from model.avatar.Bonus import Bonus
from model.avatar.Wall import Wall
from model.avatar.RandomHunter import RandomHunter
from model.avatar.BonusHunter import BonusHunter
from model.avatar.Hunter import Hunter 
from model.core.SMA import SMA
from model.avatar.AvatarControls import AvatarControls

class SMAAvatar(SMA):
    """
    Special SMA class which initialize environement with Wall, different Hunter type and the Avatar
    """

    def __init__(self, config, environment, view, configAvatar, trace_file=None, trap=False):
        """ initialize the environment

        create and put all the agent on the environement

        :param config: dictionary which contains configuration parameters for the SMA class
        :param environement: pointer to the environment
        :param view: pointer to the view
        :param configAvatar: dictionary which contains configuration parameters for the avatar simulation
        :param trace_file: file to write the log information (default = None)
        :param trap: if set to true, activate a special initial configuration of the environment
        """
        SMA.__init__(self, config, environment, view, trace_file)
        self.bonus_frequency = configAvatar['bonus_frequency']
        self.cpt_bonus = configAvatar['nb_bonus']
        self.gameEnd = False
        self.speed_hunter = configAvatar['speed_hunters']
        

        if trap:
            self.trap(config, environment, view, configAvatar, trace_file)
            return
        
        # générer les coord initial de l'agent
        coord = [(x,y) for x in range(environment.sizeX)
                 for y in range (environment.sizeY)]
        random.shuffle(coord, random.random)
 
        x,y = coord.pop()
        avatar = Avatar(environment, x, y, configAvatar['speed_avatar'], configAvatar['time_bonus'], configAvatar['nb_bonus'], self.trace_file)
        self.cont = AvatarControls(view, avatar)
        environment.put_agent(avatar)

        # Placement des murs
        for i in range(configAvatar['nb_walls']):
            x,y = coord.pop()
            environment.put_agent(Wall(environment, x, y, self.trace_file))

        # Placement des Hunters
        for i in range(configAvatar['nb_hunters']):
            x,y = coord.pop()
            environment.put_agent(Hunter(environment, x, y, configAvatar['speed_hunters'], self.trace_file))

        # Placement des RandomHunters
        for i in range(configAvatar['nb_random_hunters']):
            x,y = coord.pop()
            environment.put_agent(RandomHunter(environment, x, y, configAvatar['speed_hunters'], self.trace_file))

        # Placement des BonusHunters
        for i in range(configAvatar['nb_bonus_hunters']):
            x,y = coord.pop()
            environment.put_agent(BonusHunter(environment, x, y, configAvatar['speed_hunters'], self.trace_file))




    """
    Run qui renvoie True si la partie est terminé
    """
    def run(self):
        """
        run a turn of the game and look it is finished
        
        :return: True if during the turn, a Hunter destroy the Avatar or the avatar took the last bonus, False otherwise
        """
        # Placer un bonus ou un nouvel BonusHunter
        if ((self.ticks + 1) % self.bonus_frequency) == 0 and self.cpt_bonus != 0:
            coord = [(x,y) for x in range(self.environment.sizeX)
                     for y in range (self.environment.sizeY)]
            random.shuffle(coord, random.random)
            x,y = coord.pop()
            while(self.environment.get_agent(x, y) != None):
                x,y = coord.pop()

            if random.choice([True, False]):
                self.environment.put_agent(Bonus(self.environment, x, y, self.trace_file))
                self.cpt_bonus -= 1
            else:
                self.environment.put_agent(BonusHunter(self.environment, x, y, self.speed_hunter, self.trace_file))
            
        if self.gameEnd:
            return True 

        self.ticks += 1
        # On reprend tous les agents

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

    """ a special configuration of the environment """
    def trap(self, config, environment, view, configAvatar, trace_file):
        environment.reverse_hunter = False
        environment.torus = False
        x = environment.sizeX // 2
        y = environment.sizeY // 2
      
        avatar = Avatar(environment,x , y, configAvatar['speed_avatar'], 0, self.trace_file)
        self.cont = AvatarControls(view, avatar)
        environment.put_agent(avatar)

            # Hunter
        for x in [0, (environment.sizeX - 1)]:
            for y in range(environment.sizeY):
                environment.put_agent(Hunter(environment, x, y, 100, self.trace_file))


        for y in [0, (environment.sizeX - 1)]:
            for x in range(environment.sizeX):
                try:
                    environment.put_agent(Hunter(environment, x, y, 100, self.trace_file))
                except ValueError:
                    continue
