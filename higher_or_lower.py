from random import randrange

def guess() :
    guess = int(input("Please enter a number between 0 and 10: "))
    return guess


def rando_num() :
    rando = randrange(0,11)
    return rando
    

    
user_guess = guess()
rando_mando = rando_num();

if guess() > rando_num() :
    print("Too High! The number was: " + rando_num())
elif user_guess < rando_mando :
    print("Too Low! The number was: " + rando_num())
else :
    print("Correct! You win!")