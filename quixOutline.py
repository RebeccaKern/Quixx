import random

class Die():
              
    def roll(self):
        self.value = random.randint(1,6)
        return self.value

#initialize all dice in game

blueDie = Die()
greenDie = Die()
redDie = Die()
yellowDie = Die()
whiteDie1 = Die()
whiteDie2 = Die()

def playerRollDice():
    blueDie.roll()
    greenDie.roll()
    redDie.roll()
    yellowDie.roll()
    whiteDie1.roll()
    whiteDie2.roll()

def whiteDiceCombo():
    return whiteDie1.value + whiteDie2.value 

def blueDiceComboChoices():
    blueOptions = []
    blueOptions.append(blueDie.value + whiteDie1.value)
    blueOptions.append(blueDie.value + whiteDie2.value)
    return blueOptions

def greenDiceComboChoices():
    greenOptions = []
    greenOptions.append(greenDie.value + whiteDie1.value)
    greenOptions.append(greenDie.value + whiteDie2.value)
    return greenOptions

def redDiceComboChoices():
    redOptions = []
    redOptions.append(redDie.value + whiteDie1.value)
    redOptions.append(redDie.value + whiteDie2.value)
    return redOptions

def yellowDiceComboChoices():
    yellowOptions = []
    yellowOptions.append(yellowDie.value + whiteDie1.value)
    yellowOptions.append(yellowDie.value + whiteDie2.value)
    return yellowOptions

def printCombos():
    print(whiteDiceCombo())
    print(blueDiceComboChoices())
    print(greenDiceComboChoices())
    print(redDiceComboChoices())
    print(yellowDiceComboChoices())


playerRollDice()
printCombos()
