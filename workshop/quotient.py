done = 0
while done == 0:
    print "This program will divide two numbers."
    try:
        number1 = float(raw_input("What is the first number: "))
    except ValueError:
        print "That's not a number! Using 1.0 instead."
        number1 = 1.0
    try:
        number2 = float(raw_input("What is the second number: "))
    except ValueError:
        print "That's not a number! Using 2.0 instead."
        number2 = 2.0
    quotient = number1 / number2
    print "The quotient is: " + str(quotient) + "."