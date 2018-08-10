# Variables and Strings
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print string labled 'x'
print x
# print string labled 'y'
print y

print "I said: %r." %x
print "I also said: '%s'." % y

#variable
hilarious = False
#string 
joke_evaluation = "Isn't that joke so funny?! %r"

# The two strings are added to form a repsonse
print joke_evaluation % hilarious

# strings
w = "This is the left side of..."
e = "a string with a right side."

# The two strings are added to form a sentence
print w + e 