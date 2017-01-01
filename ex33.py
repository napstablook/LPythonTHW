i = 0
numbers = []

def append_while(i):
	for i in range(0, 6):
		print "At the top i is %d" % i
		numbers.append(i)
		
		# i = i + inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

inc = 2
six = 8
print append_while(i)		
print "The numbers: "

for num in numbers:
	print num