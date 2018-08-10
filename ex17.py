# import argv from sys
from sys import argv
# import exists from os.path
from os.path import exists
# parameters to command line
script, from_file, to_file = argv
# print and integrate the selected files
print "Copying from %s to %s " % (from_file, to_file)

# The two can be on one line, this is how
in_file = open(from_file); indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

