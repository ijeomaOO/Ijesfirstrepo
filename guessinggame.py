import random

i = random.randint(1,10)
guess = 5

while i != guess:
    guess = float(input("Enter Your Guess: "))
    if guess > i:
        print("too high")
    elif guess < i:
        print("too low")
    else:
        print("correct")
    
    

    
