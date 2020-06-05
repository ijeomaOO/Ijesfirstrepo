import random

i = random.randint(1,50)
guess = 5
guess_count = 0

while i != guess:
    guess = float(input("Enter Your Guess: "))
    guess_count += 1
    if guess > i:
        print("too high")
    elif guess < i:
        print("too low")
    else:
        print("correct")
        print("It took " + str(guess_count) + " guesses for you to find the correct number")
    
    

    
