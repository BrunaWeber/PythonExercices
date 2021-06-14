import random
#Todo: counts the number of times the user makes a guess and then add the code to tell the user how many guesses they have taken.

def GuessGame (number):

    number = random.randint(1, 101) #the right number is in sameplace in here
    guess = 1
    countGuess = 0

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        countGuess +=1
        
        if guess == number:
            print(f"Congratulations! The number you entered is:{guess}.\n You spent {countGuess} attempts to complete this game.")#Add it 11/06
            break 
        elif guess > 100:
            print("Type a number between 1 and 100!")
            continue #add continue 11/06
        elif guess < number:
            print("Your guess is too low. Try again!")
            continue
        else:
            print("Your guess is too high")
            continue

GuessGame(input)