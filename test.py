from GameField import GameField
from idaSerach import IdaSearch


f1 = GameField([6,3,7,4,2,0,1,8,5,10,15,11,9,13,14,12], 4)
solver = IdaSearch()
solution = IdaSearch.idaStart(solver, f1)

print(f1)
print("розв`язок : ", solution)
print("розв`язое дозволяє вирішити пазл ?: ", f1.go_path(solution).check_if_complete())