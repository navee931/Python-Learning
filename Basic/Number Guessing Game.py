# Generate a random number (use import random) and let the user guess it.

import random
target = random.randint(1, 10)
Num = int(input("Guess the number between 1 to 10: "))

if (target == Num):
    print("You Win")
elif(target != Num):
    print("Try again")
else:
    print("Enter a valid number")

# Generate a random number (use import random) and let the user guess it in a loop until the guess is correct. Use while loop.

import random
Target = random.randint(1, 20)
Guess = 0

while Target != Guess :
    Guess = int(input("Guess a number between 1 to 20: "))
    if Guess > Target :
        print("Too big- Try Again","You enter", Guess)
    elif Guess < Target :
        print("Too small - Try Again","You enter", Guess)
    else :
        print("You Win","You enter", Guess)
         
    