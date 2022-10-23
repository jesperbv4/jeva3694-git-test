import random
# Definition av klassen Dice
class Dice:  
    # Metoden init, skapar en tärning m sides sidor 
    def __init__(self, sides):
        self.sides = sides
        self.value = random.randint(1, self.sides)
    
    def __str__(self):
        return f'Sidor: {self.sides:2d}, värde: {self.value:2d}'
    
    def getValue(self):
        return self.value
    
    def getSides(self):
        return self.sides

    def roll(self):
        self.value = random.randint(1, self.sides)

