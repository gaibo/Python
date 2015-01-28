# Get the name of the person to greet
name = raw_input("Who should we greet? ")
# Get the number of times to repeat the greeting
times = raw_input("How many times should the greeting be repeated? ")
# We need to convert the string times to a number
repeats = int(times)
# Greet the person as many times as requested
for count in range(repeats):
    print "Hello, " + name