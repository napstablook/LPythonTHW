# allows to put more arguments on command line
from sys import argv

# these are the arguments
script, filename = argv

# print the 3 lines below and on line one prints filename in place of $r
print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#asks for user input. doesn't really matter what's inputted, I think
raw_input("?")

# print ""
print "Opening the file..."
# opens filename and w? and assigns it to target
target = open(filename, 'w')

# print ""
print "Truncating the file. Goodbye!"
# empties the file. but not necessary because of 'w' parameter in open in target
target.truncate()

# print ""
print "Now I'm going to ask you for three lines."

# asks user for three lines/strings
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# print ""
print "I'm going to write these to the file."

# uses write command/function/method to write stirngs into the file
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# print ""
print "And finally, we close it."
# closes file
target.close()