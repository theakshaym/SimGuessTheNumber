#This is a guess the number game!
import random
import sys
print('Welcome! What is your name?')
name = input()
rand = random.randint(1,20)

#This checks for valid guess
def rannum():
    print('well...,'+name+',I\'m thinking of a number between 1 to 20. Guess the number!')
    for guessTaken in range(1,7):
        print('Take a guess...')
        guess = int(input())
        if guess < rand :
            print('Your number is lower than the actual number!')
        elif guess > rand :
            print('Your number is greater than the actual number!')
        elif guess == rand :
            break
    if guess == rand:
        print("Congrats!"+name+", You guessed it in "+str(guessTaken)+" attempts!")
    else :
        print("The number was "+str(rand)+"! Better luck next time!")

#Prompt function
def yesorno():
    print('Hi, '+name+' are you ready to play the game? (y/n)')
    prom = input()
    if prom == 'y' or prom == 'Y':
        rannum()
    elif prom == 'n' or prom== 'N':
        print('Goodbye!')
        sys.exit()
    else:
        print('You entered wrong prompt.')
        yesorno()
        
yesorno()





