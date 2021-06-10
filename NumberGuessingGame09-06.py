import random

number = random.randint(1, 2) #the right number
guess = 1
while guess != number:
    guess = input("Guess a number between 1 and 100: ")


    if guess == number:
        print("congratulations! You won! It took you {} tries.".count(guess))
        break
    elif guess > 100:
        print("type a number between 1 and 100!")
    elif guess < number:
        print("Your guess is too low. Try again!")
    else:
        print("Your guess is too high")