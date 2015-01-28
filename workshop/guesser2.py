#Set 7 as the secret number
number = 7
#Prepare a while loop with flag variable
done_guessing = 0
while done_guessing == 0:
	guess = int(raw_input("Guess my number! "))
	if guess == number:
		print "You got it right!"
		done_guessing = 1
	elif guess > number:
		print "Lower!"
	else:
		print "Higher!"