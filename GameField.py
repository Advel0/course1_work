import random
import copy

class GameField:
        
    def __init__(self, list, size):
        self.size = size
        self.__fieldList = list

    def get_field_list(self):
        return copy.deepcopy(self.__fieldList)

    def __str__(self):
        strGameField = ""
        for i in range(self.size):
            for j in range(self.size):
                strGameField += f"{self.get_field_list()[j+i*4]:4d}"
            strGameField += "\n"
        
        return strGameField

    def get_cheapest_path(self):
        counter = 0
        for el in self.get_field_list():
            if el == 0:
                continue
            x = self.get_field_list().index(el) % self.size
            y = self.get_field_list().index(el) // self.size

            x_supposed = (el - 1) % self.size
            y_supposed = (el -1 ) // self.size
            counter += abs( x - x_supposed) + abs( y - y_supposed )
                
        return counter
    
    def get_possible_moves(self):
        possible_moves = []

        zero_index = self.get_field_list().index(0)
        zero_x = zero_index % self.size
        zero_y = zero_index // self.size

        if zero_y != 0:
            possible_moves.append("up")
        if zero_y != self.size-1:
            possible_moves.append("down")
        if zero_x != 0:
            possible_moves.append("left")
        if zero_x != self.size-1:
            possible_moves.append("right")

        return possible_moves

    def go_path(self, path):
        result = GameField(self.get_field_list(), self.size)

        for move in path:
            result.move_zero(move)

        return result

    def move_zero(self, move):
        zero_index = self.get_field_list().index(0)
       
        match move:
            case "up":
                self.swap(zero_index, zero_index-self.size)
            case "down":
                self.swap(zero_index, zero_index+self.size)
            case "left":
                self.swap(zero_index, zero_index-1)
            case "right":
                self.swap(zero_index, zero_index+1)

    def rand_move(self):
        n = random.randrange(4)
        match n:
            case 0:
                move = 'up'
            case 1:
                move = 'down'
            case 2:
                move = 'right'
            case 3:
                move = 'left'
        return move

    def shuffle(self):
        randMovesAmount = 100
        
        for i in range(randMovesAmount):
            move = self.rand_move()
            while move not in self.get_possible_moves():
                move = self.rand_move()

            self.move_zero(move)
        
        if not self.check_if_possible_to_complete():
            self.shuffle()


    def opposite_move(self, move):
        if move == 'right':
            return 'left'
        if move == 'left':
            return 'right'
        if move == 'up':
            return 'down'
        if move == 'down':
            return 'up'

    def check_if_possible_to_complete(self):
        zero_index = abs(self.size - self.get_field_list().index(0)//self.size)
        listGridCopy = [num for num in self.get_field_list() if num != 0]
        
        inversion_counter = 0
        for i in range(len(listGridCopy)):
            for j in range(i+1, len(listGridCopy)):
                if(listGridCopy[i] > listGridCopy[j]):
                    inversion_counter+=1


        if zero_index %2 == 1:
            if inversion_counter % 2 == 0:
                return True 
        else:
            if inversion_counter % 2 == 1:
                return True 
        return False

    def check_if_complete(self):
        temp = [num for num in self.get_field_list() if num != 0]
        for i in range(1,len(temp)):
            if(temp[i] < temp[i-1]):
                return False
        
        return True

    def swap(self, index_a, index_b):
        [self.__fieldList[index_a], self.__fieldList[index_b]] = [self.__fieldList[index_b], self.__fieldList[index_a]]