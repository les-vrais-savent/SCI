# View.py

from tkinter import *

class View:

    def __init__(self, environment, size):
        self.environment = environment
        self.window = Tk()
        self.window.title('Simulation de bille')
        
        self.height = size
        self.width = size
        
        self.canvas = Canvas(self.window, width=self.width, height=self.height, bg='white')
        self.canvas.pack(padx=5, pady=5)
        
    def update(self):
        self.canvas.delete("all") 
        
        for agent in self.environment.agents:
            square_size = self.height/self.environment.sizeX
            x0 = agent.posX * square_size
            y0 = agent.posY * square_size
            x1 = agent.posX * square_size + square_size
            y1 = agent.posY * square_size + square_size
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=agent.color)

        self.canvas.update()
