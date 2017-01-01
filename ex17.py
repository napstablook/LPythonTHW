# go see exercise 17 on book to look at the original code
from sys import argv

script, from_file, to_file = argv

indata = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()