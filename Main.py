from Game import Game
from GUI import GUI

class Main:

    def __init__(self):
        self.game = Game()
        self.game.start()
        self.gui = GUI(self.game)
        self.gui.run()


Main()
