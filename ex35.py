from sys import exit

# exit(0) is used to abort a program; the zero indicates no error (a goog exit) anything else represents different errors
def gold():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ")
    try:
        how_much = int(choice)
    except ValueError:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear():
	print "There is a bear here.\nThe bear has a bunch of honey."
	print "The fat bear is in front of another door.\nHow are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
			
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold()
		else:
			print "I got no idea what that means."
			
			
def cthulhu():
	print "Here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life, eat your head or go through the secret door?"
	
	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	elif "secret" in choice:
		black_hole()
	else:
		cthulhu_room()
		
def black_hole():
	dead("You've entered the black hole room!")
		
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right, left, and in the middle."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear()
	elif choice == "right":
		cthulhu()
	elif choice == "middle":
		black_hole()
	else:
		dead("You stumble around the room until you starve.")
		
		
start()