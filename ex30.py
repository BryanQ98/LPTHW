# VAriables
people = 30
cars = 40
buses = 15
# if cars greater than people then print string
if cars > people:
	print "We should take cars."
# if statement false, then print following statement
elif cars < people:
	print "We should not take the cars."
# if both statements false, then print this statement
else:
	print "We can't decide."
# if buses greater than cars print this new statement
if buses > cars:
	print "That's too many buses."
# if statement above false, then print this new NEW statement
elif buses < cars:
	print "Maybe we can take the buses."
# if both statements above false, then print another new statement
else:
	print "We still can't decide."
# if people greater than buses, yet another new statement to print
if people > buses:
	print "Alright, let's just take the buses."
# if statement above false then print final statement
else:
	print "Fine, let's stay home then."