# adding function
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	# 'return' returns a value when called
	return a + b
# subtracting function
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
# multiplication function
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
# division function
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
	
print "Let's do some math with just functions!"
# variables adding parameters to the function
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# An extra credit puzzle.
print "Here is a puzzle."
# using the return value of one function as an argument in another function
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"