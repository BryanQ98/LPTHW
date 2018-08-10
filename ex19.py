# defined function with UNSET arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party"
	print "Get a blacket. \n"

# calling function with SET arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# calling arguments directly
print "OR, we can use variables from the script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# using math to define arguments 
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# using variables and math to define arguments
print "And we can combine the two varibles and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Applying what was taught
print "Just playing with functions"
cheese_and_crackers(27 * 80, amount_of_crackers + 20000)