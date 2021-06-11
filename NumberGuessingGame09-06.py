import random

number = random.randint(1, 101) #the right number
guess = 1
while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))


    if guess == number:
        print(f"congratulations! The number you entered is:{guess}")#Add it 11/06
        break 
    elif guess > 100:
        print("type a number between 1 and 100!")
        continue #add continue 11/06
    elif guess < number:
        print("Your guess is too low. Try again!")
        continue
    else:
        print("Your guess is too high")
        continue