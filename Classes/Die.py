import random

class Die():
              
    def roll(self):
        self.value = random.randint(1,6)
        return self.value