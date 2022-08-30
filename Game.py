import random
import tkinter as tk
from GUI import GUI
from Grid import Grid
from idaSerach import IdaSearch

class Game:    

    def __init__(self):
        self.level1Grid = [1,2,3,4,5,6,7,8,9,10,12,0,13,14,11,15]
        self.level2Grid = [1,7,2,4,5,3,8,11,9,6,10,12,13,14,15,0]
        self.level3Grid = [2,6,7,3,1,9,11,4,5,15,14,10,13,0,12,8]
        self.move_count = 0


    def start(self):
        size = 4 
        listGrid = [num for num in range(1,size**2)]
        listGrid.append(0)
        self.grid = Grid(listGrid, size)

        self.gui = GUI(self.grid, self)

        self.gui.run()

    def solve_game(self):
        idaSolver = IdaSearch()

        path = idaSolver.idaStart(self.grid)

        return path

    def restart(self):
        self.gui.restartFrame.destroy()
        self.gui.mainFrame.destroy()
        self.grid.shuffleGrid()
        self.gui.draw_frame()
        
