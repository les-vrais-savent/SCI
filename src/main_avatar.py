import random
import json
import argparse

from model.avatar.EnvironmentAvatar import EnvironmentAvatar
from model.avatar.SMAAvatar import SMAAvatar
from view.View import View

ap = argparse.ArgumentParser()
ap.add_argument("--courbe", type=bool, default=False)
ap.add_argument("--grid_size_X", type=int, default=100)
ap.add_argument("--grid_size_Y", type=int, default=100)

args = vars(ap.parse_args())

config = json.loads(open('config.json').read())
configAvatar = json.loads(open('configAvatar.json').read())

if args['courbe']:
    config['trace'] = True
    config['grid_size_X'] = args['grid_size_X']
    config['grid_size_Y'] = args['grid_size_Y']
    config['view']=False
    config['seed']=0
else:
    config['view']=True

trace_file = open("trace.csv", "w+") if config['trace'] else None

seed = None if config['seed'] == 0 else config['seed']
random.seed(seed)

env = EnvironmentAvatar(config['grid_size_X'], config['grid_size_Y'], config['torus'])
view = View(env, config['canvas_size_X']) if config['view'] else None
sma = SMAAvatar(config, env, view, configAvatar, trace_file)

def test():
    while not sma.run():
        continue

if view != None:
    view.window.after(1000, test)
    view.window.mainloop()
else:
    test()

if trace_file != None:
    trace_file.close()
