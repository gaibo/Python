#Import a module that allows the computer to choose a random number
import random
#Define a function that relates two variables
def process_guess(number, guess):
    success = 0
    if guess == number:
	    print "You got it right!"
	    success = 1
    elif guess < number:
	    print "Too low!"
    else:
	    print "Too high!"
    return success
#Actual "beginning" of program
#Use the module to choose a random number from 0 to 100
number = random.randrange(100)
#Define a flag variable and create a while loop
done_guessing = 0
while done_guessing == 0:
    guess = int(raw_input("Guess the number! "))
    done_guessing = process_guess(number, guess)