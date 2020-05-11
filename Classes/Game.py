from Classes.Die import Die

class Game():

    def __init__():
        self.players = []
        initDice(self)

    def initDice(self):
        # initialize all dice in game
        self.redDie = Die()
        self.yellowDie = Die()
        self.greenDie = Die()
        self.blueDie = Die()
        self.whiteDie1 = Die()
        self.whiteDie2 = Die()

    def initPlayers(self):
        pass

    def isGameOver(self):
    # if player has 5 strikes or two rows are locked the game is over
        for board in self.boards:
            pass

    def playerWinsMessage():
    # returns which player won the game
        pass

    def takeTurn():
        Player.rollDice()
        Player.takeTurn()
        # other players take turn with white dice
        # if player locks row, then rows need to be locked on the other boards
