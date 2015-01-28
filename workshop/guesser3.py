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
number = 7
done_guessing = 0
while done_guessing == 0:
    guess = int(raw_input("Guess the number! "))
    done_guessing = process_guess(number, guess)