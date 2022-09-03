import random
import tkinter as tk
from GameField import GameField
from idaSerach import IdaSearch
import copy

class Game:    

    def __init__(self):
        self.__levels = [

            [1,2,3,4,5,6,7,8,9,10,12,0,13,14,11,15],
            [1,7,2,4,5,3,8,11,9,6,10,12,13,14,15,0],
            [0,1,8,3,6,2,7,4,5,9,10,12,13,14,11,15]
        ]
        self.__move_count = 0
        self.__taken_steps = []

    def get_game_field(self):
        return copy.deepcopy( self.__gameField )

    def start(self):
        size = 4 
        fieldList = [num for num in range(1,size**2)]
        fieldList.append(0)
        self.__gameField = GameField(fieldList, size)

        self.idaSearch = IdaSearch()
        

    def load_level(self, level_id):
        self.__gameField = GameField(self.__levels[level_id].copy(), 4)

    def solve_game(self):
        print(self.get_game_field().get_cheapest_path())        
        path = self.idaSearch.idaStart(self.get_game_field())

        return path

    def make_move(self, direction):
        self.__gameField.move_zero(direction)

    def save(self):
        with open("completed_games.txt", "a") as f:
            res = "\n================\n"
            res += "field: \n"
            res += str(self.get_game_field().go_path([self.get_game_field().opposite_move(move) for move in self.get_taken_steps()[::-1]]))
            res += "----------------\n"
            res += "solution: \n"
            res += str(self.get_taken_steps())
            res += "\n================\n"
            f.write(res)

    def randomize_game_field(self):
        self.__gameField.shuffle()

    def get_move_count(self):
        return self.__move_count

    def reset_move_count(self):
        self.__move_count = 0
    
    def increase_move_count(self):
        self.__move_count +=1

    def new_step(self, step):
        self.__taken_steps.append(step)

    def get_taken_steps(self):
        return copy.deepcopy( self.__taken_steps )

    def reset_taken_steps(self):
        self.__taken_steps = []

    def attempt_move(self, coords):

        zero_index = self.get_game_field().get_field_list().index(0)
        element_index = (coords[0]+coords[1]*self.get_game_field().size)
        distance = zero_index - element_index

        if ( abs(distance) == 4 or abs(distance) == 1 ):
            self.__move_count +=1 
            
            if distance == 4:
                self.new_step("up")
            elif distance == -4:
                self.new_step("down")
            elif distance == 1:
                self.new_step("left")
            elif distance == -1:
                self.new_step("right")

            self.__gameField.swap(zero_index, element_index)

            return True

        return False