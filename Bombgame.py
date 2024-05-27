#prolog
#names: Ryan Morris-Scott, Parker Saetang
#section: 018

import random 

#introduce game to user
print("   ***   Defuse the Bomb!   ***  \n\n")
print(" - The Defusal code is 4 digits long")
print(" - Each digit is between 1 and 5")
print(" - Guess one digit of the defusal code at a time")
print(" - 3 incorrect guesses total will detonate the bomb")
print(" - Each correct guess warrants 1 additional guesses.\n")

#initializing values
guesses = 3
rounds = 4

#main function assigning numbers to each bomb code digit
def main():
    digit = random.randint(1, 5)
    return digit

#function does the math of awarding or removing guesses based on if guessed correctly or not
def digitGuess(guess, digit):
    global rounds
    global guesses
    if guess != digit:
        guesses -= 1
        print(f"That's incorrect. Try again. Guesses remaining: {guesses}")
        print()
    else:
        print("You guessed correctly!")
        print()
        guesses += 2
        rounds -= 1
        digit = main()
    return guess, guesses, digit

#end-game scenarios
while guesses > 0 and rounds > 0:
    digit = main()
    while guesses > 0:
        guess = int(input("Enter your guess for the digit: "))
        guess, guesses, digit = digitGuess(guess, digit)
        if guesses == 0:
            print("Game over. The digit was: ", digit)
            break
        if rounds == 0:
            print("Congratulations, you defused the bomb!")
            break
