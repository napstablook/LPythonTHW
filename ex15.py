# allows to put more arguments/variable/values on the command line
from sys import argv

# tells argv the name/variable of the arguments
script, filename = argv

# uses open() to open filename value (text inside filename) which is put into txt 
txt = open(filename)

# prints "" and the filename value
print "Here's your file %r:" % filename
""" 
prints the contents of txt, which i think is ex15_sample.txt and 
reads the contents of that file using read command
"""
print txt.read()

# prints ""
print "Type the filename again:"
# asks user for filename again using raw_input & assigns it to file_again
file_again = raw_input("> ")

# opens file_again, returns file object and assigns it to txt_again
txt_again = open(file_again)

# reads and prints value of txt_again
print txt_again.read()

txt.close()
txt_again.close()