"""
if choice is an integer assing it to how_much using int() funcion
else "Learn to type numbers, mang..."
then
if < 50: Win
if > 50: Lose
"""

"""
def gold():
	print "This room is full of gold.  How much do you take?"
	
	choice = raw_input("> ")
	if choice.isdigit():
		how_much = int(choice)
	else:
		print "Learn to type some numbers, mang... rip."
		
	if how_much < 50:
		print "You win!"
		exit(0)
	else:
		print "death by greed.  Good job!"
		exit(0)
		

gold()
"""

def gold_room():
	print "This room is full of gold.  How much do you take?"

	choice = raw_input("> ")
	if choice.isdigit():
		how_much = int(choice)
	else:
		print "Man, learn to type a number."
		exit(0)

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		print "You greedy bastard!"
		exit(0)
			

gold_room()