'''Assignment on python
Build a python guessing game. 
The features of the game includes
1. Ask the user to guess a number, which you already predefined in the code
2. The user has the opportunity to guess a number up to 5times
3. If after 5 trials the user didn't guess the correct number, end the game with a good message for the user
4. For each time the user guesses a number, if the number is not correct print the appropriate message and show the user the numbers of trials remaining
5. If the user guesses the correct number, print the appropriate message and end the game, even if it is on the 1st trial.
'''

#solution

print("\n\tPYTHON GUESSING GAME")
print("\nWelcome to guessing game app")
num = 7

for i in range(1,6):
    guess = int(input("\nPlease enter a number between 1 and 10: "))
    if guess != num:
        print("\nPlease try again")
        print("\nYou have", 5 - i, "trials left")
    else:
        print("\nYour guess is right on trial", i + 1)
        print("\nThanks for using this software")
        break


print("\nThanks for using this software")