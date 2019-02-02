import random

class Die():
              
    def roll(self):
        self.value = random.randint(1,6)
        return self.value

#initialize all dice in game

redDie = Die()
yellowDie = Die()
greenDie = Die()
blueDie = Die()
whiteDie1 = Die()
whiteDie2 = Die()

def playerRollDice():
    redDie.roll()
    yellowDie.roll()
    greenDie.roll()
    blueDie.roll()
    whiteDie1.roll()
    whiteDie2.roll()

def whiteDiceCombo():
    return whiteDie1.value + whiteDie2.value 

def colorDiceCombo(die):
    options = []
    options.append(die.value + whiteDie1.value)
    options.append(die.value + whiteDie2.value)
    return options

def allColorCombos():
    allColorOptions = []
    allColorOptions.append(colorDiceCombo(redDie))
    allColorOptions.append(colorDiceCombo(yellowDie))
    allColorOptions.append(colorDiceCombo(greenDie))
    allColorOptions.append(colorDiceCombo(blueDie))
    return allColorOptions

def printCombos():
    print(whiteDiceCombo())
    print(allColorCombos())

playerRollDice()
printCombos()


def increasingRow():
    row = []
    for i in range(2,13):
        row.append(i)
    return row

def decreasingRow():
    row = []
    for i in range(2,13):
        row.append(14-i)
    return row


class Board():
              
    def __init__ (self):
        self.board = []
        redRow = increasingRow()
        yellowRow = increasingRow()
        greenRow = decreasingRow()
        blueRow = decreasingRow()
        self.board.append(redRow)
        self.board.append(yellowRow)
        self.board.append(greenRow)
        self.board.append(blueRow)

    def canCheckBox(self, color, number):
        if color == 'red':
            row = 0
        if color == 'yellow':
            row = 1
        if color == 'green':
            row = 2
        if color == 'blue':
            row = 3
        if number in self.board[row]:
            return True
        return False

    def fillPrev(self, row, number):
        for i in range(0, number):
            if self.board[row][i] != 'X':
                self.board[row][i] = 'Z'
        return self.board

    def checkBox(self, color, number):
        if color == 'red':
            row = 0
        if color == 'yellow':
            row = 1
        if color == 'green':
            row = 2
        if color == 'blue':
            row = 3
        num = self.board[row].index(number)
        self.board[row][num] = 'X'
        self.fillPrev(row, num)
        return self.board


board1 = Board()

print(board1.board)

board1.checkBox('red', 8)

print(board1.board)


