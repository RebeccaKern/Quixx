class Board():
              
    def __init__ (self):
        self.board = []
        strikes = 0
        self.scoreDict = {0:0, 1:1, 2:3, 3:6, 4:10, 5:15, 6:21, 7:28, 8:36, 9:45, 10:55, 11:66, 12:78}
        redRow = self.increasingRow()
        yellowRow = self.increasingRow()
        greenRow = self.decreasingRow()
        blueRow = self.decreasingRow()
        self.board.append(redRow)
        self.board.append(yellowRow)
        self.board.append(greenRow)
        self.board.append(blueRow)

    def increasingRow(self):
        row = []
        for i in range(2,13):
            row.append(i)
        #to indicate whether or not row is locked
        row.append(False)
        return row

    def decreasingRow(self):
        row = []
        for i in range(2,13):
            row.append(14-i)
        #to indicate whether or not row is locked
        row.append(False)
        return row

    def takeStrike(self):
        self.strikes += 1

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
        self.canLockRow(row)
        return self.board

    def numCellsFilled(self, row):
        return self.board[row].count('X')

    def finalCellInRowFilled(self, row):
        return self.board[row][-2] == 'X'

    def canLockRow(self, row):
        if (self.numCellsFilled(row) == 5) and self.finalCellInRowFilled(row):
            return True
        return False

    def lockRow(self):
        row[-1] = True

    def scoreRow(self, row):
        score = 0
        a = self.numCellsFilled(row)
        score += self.scoreDict[a]
        return score

    def scoreBoard(self):
        totalScore = 0
        for rowNum in range(0, len(self.board)):
            totalScore += self.scoreRow(rowNum)
        return totalScore



