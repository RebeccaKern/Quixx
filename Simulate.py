from Classes.Die import Die
from Classes.Board import Board

#initialize all dice in game
redDie = Die()
yellowDie = Die()
greenDie = Die()
blueDie = Die()
whiteDie1 = Die()
whiteDie2 = Die()

board1 = Board()

print(board1.board)

board1.checkBox('red', 6)
board1.checkBox('red', 7)
board1.checkBox('red', 8)
board1.checkBox('red', 9)
board1.checkBox('red', 12)
print(board1.board)

print(board1.canLockRow(0))