#This is a guess the number game!
import random
import sys
name = input('Welcome! What is your name? ')
lowerLimit = 1
upperLimit = 20
rand = random.randint(lowerLimit,upperLimit)
attem = 6

#This checks for valid guess
def rannum():
    print('well...,'+name+',I\'m thinking of a number between '+str(lowerLimit)+' and '+str(upperLimit)+'.')
    for guessTaken in range(attem):
        print('Take a guess... ')
        try:
            guess = int(input())
        except ValueError:
            print("You did not enter a valid number.")
            sys,exit()
        if guess < rand :
            print('Your number is lower than the actual number!')
        elif guess > rand :
            print('Your number is greater than the actual number!')
        elif guess == rand :
            break
    if guess == rand:
        print("Congrats!"+name+", You guessed it in "+str(guessTaken+1)+" attempts!")
    else :
        print("The number was "+str(rand)+"! Better luck next time!")

#Prompt function
def yesorno():
    prom = input('Hi, %s are you ready to play the game? (y/n) ' %(name))
    if prom == 'y' or prom == 'Y':
        rannum()
    elif prom == 'n' or prom== 'N':
        print('Goodbye!')
        sys.exit()
    else:
        print('You entered wrong prompt.')
        yesorno()
        
yesorno()





