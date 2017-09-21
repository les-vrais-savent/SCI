import random
import json

from model.SMA import SMA
from model.Environment import Environment
from view.View import View


config = json.loads(open('config.json').read())

env = Environment(config['grid_size_X'])
view = View(env, config['canvas_size_X'])
sma = SMA(config['nb_particles'], env, view, config['delay'], config['sheduling'])


seed = None if config['seed'] == 0 else config['seed']
random.seed(seed)

def test():
    for i in range(config['nb_ticks']):
        sma.run()
    #view.window.after(1000, test)

view.window.after(1000, test)
view.window.mainloop()
