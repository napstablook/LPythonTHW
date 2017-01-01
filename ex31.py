print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake, What do you do?"
	print "1. Take the cake,"
	print "2. Scream at the bear."
	print "3. Stab the bear."
	print "4. Seduce the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off.  Good job!"
	elif bear == "2":
		print "The bear eats your legs off.  Good job!"
	elif bear == "3":
		print "The bear takes all your money and eats you.  Good job!"
	elif bear == "4":
		print "The bear shows mild interest. What shall you do now?"
		print "1. Stab the bear now that it is distracted."
		print "2. Marry the bear, then plan to leave one night while it sleeps."
		
		whatnow = raw_input("> ")
		
		if whatnow == "1":
			print "You kill the bear, but he falls on you... You die.  Good job!"
		elif whatnow == "2":
			print """The bear never sleeps, so you are stuck living with him until you die.
Thus, you learn to love it and understand that all it wanted in life was some companionship.\nTrue ending...  <3."""
		else:
			print """\"I got you fam!\", reverberates through the hills. The dark lord has come to save you!
You are suddenly equipped with a shotgun. You sacrifice the bear to the dark lord.  Good job!"""
	else:
		print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina." 
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"
		
else:
	print "Your stumble around and fall on a knife and die.  Good job!"