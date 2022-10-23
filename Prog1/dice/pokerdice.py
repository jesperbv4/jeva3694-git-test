import dice # Klassen PokerDice måste känna till klassen Dice

class PokerDice:
    def __init__(self, dices):
        self.dice_list = [(dice.Dice(6)) for i in range(dices)]
    
            

    def __str__(self):
	    # Använder metoden getValue i Dice
        return str(sorted([d.getValue() for d in self.dice_list])) 

    def roll(self):
        for d in self.dice_list:
            d.roll()      # Använder rollmetoden i Dice

    def dices(self):
        return len(self.dice_list)

# Test av klassen PokerDice
print('Pokertärningar:')
pd = PokerDice(8) 
for i in range(10):
    pd.roll()
    print(pd)
