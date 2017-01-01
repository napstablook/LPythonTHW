# assings values to those variables
people = 60
cars = 12
trucks = 30

# tests the things and it stops when it finds a true statement
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
# same as above; the first if is basically true or true
if trucks > cars or (not(trucks > people or cars > people)):
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."
	
# same as above the if is true and false, which equals false, so it uses the else statement
if people > trucks and people == trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."