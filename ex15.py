# From system imports argv
from sys import argv
# adds a parameter to command line
script, filename = argv
# open is for reading files in text mode
txt = open(filename)
# print command prints
print "Here's your file %r:" %filename
# print function
print txt.read()
# print
print "Type the filename again:"
# asks for the name of file, which must be answered by raw_input
file_again = raw_input("> ")
# opens text file again
txt_again = open(file_again)

print txt_again.read()