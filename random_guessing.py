import random

complete = 1 
Number = random.randint(1, 100)
def Guess():
    player_guess = int(input("please enter a number: "))
    return player_guess

def main(Number):
    global complete
    player_Guess = Guess()
    Number = int(Number)
    
    if Number == player_Guess:
        print("well done you are correct")
        complete = 0
    elif Number < player_Guess:
        print("your guess was too large")
    elif Number > player_Guess:
        print("your guess was too small")
    
    return player_Guess

while complete == 1:
    player_Guess = main(Number)
