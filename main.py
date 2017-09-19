from model.SMA import SMA
from model.Environment import Environment
from view.View import View

import argparse
# from  model.Agent import Agent

ap = argparse.ArgumentParser()

ap.add_argument("--size", type=int, default=10,
                help="(optional) size of the grid")
ap.add_argument("--nb_agent", type=int, default=10,
                help="(optional) number of agent")
ap.add_argument("--nb_round", type=int, default=10,
                help="(optional) number of round")

args = vars(ap.parse_args())

env = Environment(args["size"])
view = View(env)
sma = SMA(args["nb_agent"], env, view)

def test():
    for i in range(args["nb_round"]):
        sma.run()
    #view.window.after(1000, test)

view.window.after(1000, test)
view.window.mainloop()
