from sys import argv
# parameters to commandline
script, filename = argv
# print 
print "We're gaing to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# user input
raw_input("?")
# Opens file selected
print "Opening file..."
target = open(filename,'w')
# delete everything within the selected file
print ("Truncating the file. Goodbye!")
target.truncate()

print "Now I'm going to ask you for three lines."
# variables to edit file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"
# user input to edit selcted file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# print
print "And finally, we close it."
