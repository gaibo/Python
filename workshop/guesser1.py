number = 7
user_guess = raw_input("Guess my number ")
guess = int(user_guess)
print guess
if guess == number:
    print "You got it right!"
elif guess > number:
    print "Lower!"
else:
    print "Higher!"