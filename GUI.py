import tkinter as tk
import random

class GameButton:
    def __init__(self, value, coords):
        self.value = value
        self.coords = coords
    
    def get_tk_button(self, frame, func):
        if (self.value == 0):
            return tk.Button(frame, text="" , font=("Ariel", 18), state="disabled")
        return tk.Button(frame, text=str(self.value) , font=("Ariel", 18), command=lambda: func(self.coords))

from Grid import Grid


class GUI:

    def __init__(self, grid, game):
        self.grid = grid
        self.game = game


    def run(self):
        self.root = tk.Tk()
        self.root.geometry("500x350")
        self.root.resizable(False,False)
        self.root.title("гра в п`ятнашки")
        self.mainFrame = tk.Frame(self.root)

        self.draw_menu_frame()

        self.root.mainloop()
    
    def get_game_button_grid(self,grid):
        buttonList = []

        for i in range(grid.size):
            for j in range(grid.size):
                buttonList.append(GameButton(grid.listGrid[j+i*4], (j, i)))
        
        return buttonList

    def draw_frame(self):
        # print(self.grid.check_if_complete())        
        if not self.grid.check_if_complete():
            self.draw_game_frame()
        else:
            self.draw_win_frame()

    def start_rand_level(self):
        self.mainFrame.destroy()
        self.mainFrame = tk.Frame(self.root)
        self.grid.shuffle_grid()
        self.draw_frame()

    def draw_level(self, level):
        if level == 1:
            self.grid = Grid(self.game.level1Grid.copy(), int(len(self.game.level1Grid)**0.5))
            self.game.grid = self.grid
            self.draw_frame()
        elif level ==2:
            self.grid = Grid(self.game.level2Grid.copy(), int(len(self.game.level1Grid)**0.5))
            self.game.grid = self.grid
            self.draw_frame()
        elif level ==3:
            self.grid = Grid(self.game.level3Grid.copy(), int(len(self.game.level1Grid)**0.5))
            self.game.grid = self.grid
            self.draw_frame()

    def draw_game_frame(self):
        self.mainFrame.destroy()
        self.mainFrame = tk.Frame(self.root)
        # self.mainFrame.columnconfigure(0, weight=1)

        move_count = tk.Label(self.mainFrame, text=f'переміщень : {self.game.move_count}', font = ("Ariel", 18))
        move_count.pack(fill='x')

        gameFrame = tk.Frame(self.mainFrame)

        for i in range(self.grid.size):
                gameFrame.columnconfigure(i, weight=1)

        for button in self.get_game_button_grid(self.grid):
            button.get_tk_button(gameFrame, self.on_click).grid(column=button.coords[0], row=button.coords[1], sticky=tk.W + tk.E)

        gameFrame.pack(fill="x")

        helpButton = tk.Button(self.mainFrame, text="Підказка" , font=("Ariel", 18), command=lambda: self.draw_game_frame_with_assist(self.game.solve_game()))
        helpButton.pack(pady=5)
        menuButton = tk.Button(self.mainFrame, text="Головне Меню" , font=("Ariel", 18), command=self.draw_menu_frame)
        menuButton.pack(pady=20)

        self.mainFrame.pack(fill="x")

    def move_zero(self, directions):
        self.grid.move_zero(directions.pop(0))
        self.game.move_count+=1
        self.draw_game_frame_with_assist(directions)
        

    def draw_game_frame_with_assist(self, directions):
        if directions:
            self.mainFrame.destroy()
            self.mainFrame = tk.Frame(self.root)
            # self.mainFrame.columnconfigure(0, weight=1)

            move_count = tk.Label(self.mainFrame, text=f'переміщень : {self.game.move_count}', font = ("Ariel", 18))
            move_count.pack(fill='x')

            gameFrame = tk.Frame(self.mainFrame)

            for i in range(self.grid.size):
                    gameFrame.columnconfigure(i, weight=1)

            for button in self.get_game_button_grid(self.grid):
                button.get_tk_button(gameFrame, self.on_click).grid(column=button.coords[0], row=button.coords[1], sticky=tk.W + tk.E)

            gameFrame.pack(fill="x")

            match directions[0]:
                case "up":
                    helpText="\u2191"
                case "down":
                    helpText="\u2193"
                case "right":
                    helpText="\u2192"
                case "left":
                    helpText="\u2190"


            helpButton = tk.Button(self.mainFrame, text=helpText , font=("Ariel", 18), command=lambda: self.move_zero(directions) )
            helpButton.pack(pady=5)
            menuButton = tk.Button(self.mainFrame, text="Головне Меню" , font=("Ariel", 18), command=self.draw_menu_frame)
            menuButton.pack(pady=20)

            self.mainFrame.pack(fill="x")
        else:
            self.draw_frame()


    def draw_win_frame(self):
        self.mainFrame.destroy()
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.columnconfigure(0, weight=1)

        move_count = tk.Label(self.mainFrame, text=f'переміщень : {self.game.move_count}', font = ("Ariel", 18))
        move_count.pack(fill='x')

        winFrame = tk.Frame(self.mainFrame)

        for i in range(self.grid.size):
                winFrame.columnconfigure(i, weight=1)

        for button in self.get_game_button_grid(self.grid):
            tkButton = button.get_tk_button(winFrame, self.on_click)
            tkButton["state"]="disabled"
            tkButton.grid(column=button.coords[0], row=button.coords[1], sticky=tk.W + tk.E)

        winFrame.pack(fill="x")

        label = tk.Label(self.mainFrame, text="Ви перемогли !", font = ("Ariel", 18))
        label.pack(pady=5)

        menuButton = tk.Button(self.mainFrame, text="Головне Меню" , font=("Ariel", 18), command=self.draw_menu_frame)
        menuButton.pack(pady=10)

        self.mainFrame.pack(fill="x")



    def draw_menu_frame(self):
        self.game.move_count=0
        self.mainFrame.destroy()
        self.mainFrame = tk.Frame(self.root)
        
        self.mainFrame.columnconfigure(0, weight=1)
        label = tk.Label(self.mainFrame, text="Головне Меню", font=("Arial", 18), pady=20)
        label.grid(column=0, row=0,sticky=tk.W + tk.E)


        levelsFrame = tk.Frame(self.mainFrame)
        levelsFrame.columnconfigure(0, weight=1)
        levelsFrame.columnconfigure(1, weight=1)
        levelsFrame.columnconfigure(2, weight=1)

        label = tk.Label(levelsFrame, text="Рівні", font=("Arial", 18), pady=20)
        label.grid(column=1, row=0,sticky=tk.W + tk.E)

        lv1Button = tk.Button(levelsFrame, text="Рівень 1" , font=("Ariel", 18), command=lambda: self.draw_level(1))
        lv1Button.grid(column=0, row=1)

        lv2Button = tk.Button(levelsFrame, text="Рівень 2" , font=("Ariel", 18), command=lambda: self.draw_level(2))
        lv2Button.grid(column=1, row=1)

        lv3Button = tk.Button(levelsFrame, text="Рівень 3" , font=("Ariel", 18), command=lambda: self.draw_level(3))
        lv3Button.grid(column=3, row=1)

        levelsFrame.grid(column=0, row=1)
        

        playRandButton = tk.Button(self.mainFrame, text="Грати Випадковий Рівень" , font=("Ariel", 18), command=self.start_rand_level)
        playRandButton.grid(column=0, row=2, pady=20)

        self.mainFrame.pack(fill="x")


    def on_click(self, coords):
        zero_index = self.grid.listGrid.index(0)
        element_index = (coords[0]+coords[1]*4)
        distance = abs (zero_index - element_index)

        if ( distance == 4 or distance == 1 ):
            self.game.move_count +=1 
            print("1")

            self.grid.swap(zero_index, element_index)

            self.draw_frame()


