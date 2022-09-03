import math

class IdaSearch:

    def __init__(self):
        pass

    def idaStart(self, gameField):
        self.gameField = gameField
        bound = self.gameField.get_cheapest_path()
        while True:
            res = self.search([], bound)
            if type(res) is type([]):
                return res
            bound = res

    def search(self, path, bound):
        currentState = self.gameField.go_path(path)
        f = len(path) + currentState.get_cheapest_path()
        if f > bound:
            return f
        if currentState.check_if_complete():
            return path
        min = math.inf

        for move in currentState.get_possible_moves():
            if len(path) == 0 or self.gameField.opposite_move(move) != path[-1]:
                res = self.search(path + [move], bound)
                if type(res) is type([]):
                    return res 
                if res < min:
                    min = res
        return min