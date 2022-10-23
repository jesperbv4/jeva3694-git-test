
print("     " + "1")

game_over = False
guess = input()
n = 1

def flippblipp(n):
    if n%3 == 0 and n%5 == 0:
        return("flipp blipp")
    elif n%3 == 0:
        return("flipp")
    elif n%5 == 0:
        return("blipp")
    else:
        return(str(n))

while game_over == False:
    if guess.lower() == flippblipp(n+1):
        print("Nästa:" + flippblipp(n+1))
        guess = input()
        n = n+1
    else:
        print("Fel - " + flippblipp(n+1))
        print("Game Over")
        game_over = True



#for i in range(1, n+1):
#    print(flippblipp(i))

