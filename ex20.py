# this allows to use argv to kind of call scripts or files on the command line
from sys import argv

# these are the two argument names
script, input_file = argv

# this creates a function that reads whatever f may be
def print_all(f):
	print f.read()

# this is another function that uses the command seek on f
def rewind(f):
	f.seek(0)

# this is another fuction that prints whatever 'line_count' may be & reads line of 'f'
# the comma at the end of the function makes it so that it doesn't double the \n
def print_a_line(line_count, f):
	print line_count, f.readline(),

# current_file is now the opened file that was inputted in the command line
current_file = open(input_file)

# print ""
print "First let's print the whole file:\n"

# uses function 'print_all' to read the opened current_file
print_all(current_file)

# print ""
print "Now let's rewind, kind of like a tape."

# uses function 'rewind' to point or set pointer to the beginning of the file since 'seek(0)
rewind(current_file)

# print ""
print "Let's print three lines:"

# gives the variable a value
current_line = 1
# uses function to print line_count and a line of the file
# passes current_line to line_count
print_a_line(current_line, current_file)

# does the same as the previous two lines but change the number to two by adding
# current line = 2
current_line += 1
# passes current_line to line_count
print_a_line(current_line, current_file)

# does the same as last 2 lines
# current line = 3
current_line += 1
# passes current_line to line_count
print_a_line(current_line, current_file)