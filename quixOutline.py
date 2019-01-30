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
