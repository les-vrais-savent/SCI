# View.py

from tkinter import *

class View:

    def __init__(self, environment, size):
        self.environment = environment
        self.window = Tk()
        self.window.title('Simulation')
        
        self.height = size
        self.width = size
        
        self.canvas = Canvas(self.window, width=self.width, height=self.height, bg=self.environment.color)
        self.canvas.pack()

    def update(self):
        self.canvas.delete("all") 
        #self.canvas.create_rectangle(0, 0, self.width, self.height, fill='white')
 
        for l in self.environment.grid:
            for agent in l:
                if agent != None:
                    square_size = self.height/self.environment.sizeX
                    x0 = agent.posX * square_size
                    y0 = agent.posY * square_size
                    x1 = agent.posX * square_size + square_size
                    y1 = agent.posY * square_size + square_size
                    if agent.form == 'oval':
                        self.canvas.create_oval(x0, y0, x1, y1, outline='', fill=agent.getColor())
                    else:
                        self.canvas.create_rectangle(x0, y0, x1, y1, outline='', fill=agent.getColor())

        self.canvas.update()
