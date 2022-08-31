import random
import tkinter as tk
from GUI import GUI
from Grid import Grid
from idaSerach import IdaSearch

class Game:    

    def __init__(self):
        self.level1Grid = [1,2,3,4,5,6,7,8,9,10,12,0,13,14,11,15]
        self.level2Grid = [1,7,2,4,5,3,8,11,9,6,10,12,13,14,15,0]
        self.level3Grid = [0,1,8,3,6,2,7,4,5,9,10,12,13,14,11,15]
        self.move_count = 0
        self.taken_steps = []


    def start(self):
        size = 4 
        listGrid = [num for num in range(1,size**2)]
        listGrid.append(0)
        self.grid = Grid(listGrid, size)


        self.idaSearch = IdaSearch()
        self.gui = GUI(self.grid, self)

        self.gui.run()

    def solve_game(self):
        print(self.grid)
        path = self.idaSearch.idaStart(self.grid)

        return path

