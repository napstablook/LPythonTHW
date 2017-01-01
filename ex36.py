from sys import exit
# This imports module "sleep" that creates a time delay (used in matrix_edn)
from time import sleep
# Use lists and modules

def cthulhu_alt():
    # Secret path
    print "You wake up in a dark room. At the opposite end lies cthulhu."
    print "cthulhu is in the middle, sleeping."
    print "You were in some sort of matrix."
    print "Should you go back to sleep or try to fight cthulhu?"

    choice = raw_input("> ")

    if choice == "back":
        cthulhu("Welcome back!")
    elif choice == "fight":
        matrix_edn("Turns out that Cthulhu's pretty weak.")
    else:
        dead("Oh, I see what you were trying to do. Here it is.")

def matrix_edn(trans):
    repeat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 43]
    print trans, "You know the movie \"The Matrix\"?"
    print "Yeah, that's your life now."
    for i in repeat:
        print "This is the end." ; sleep(0.4)
    sleep (2.4) ; print "THE EDN."
    exit(0)

def doorone():
    print "This is room one."
    print "There is a door in front of you and one on the side."
    print "Which door do you open?"

    choice = raw_input("> ")

    if choice == "front":
        animu()
    elif choice == "side":
        doortwo()
    else:
        print "That was not an option."

def doortwo():
    print "This is room two."
    print "There is one door here."
    print "Do you take it or nah"

    choice = raw_input("> ")

    if choice == "take":
        doorone()
    elif choice == "nah":
        blk_hl()
    else:
        print "What"

def animu():
    print "You can fight naruto or whatever."

    choice = raw_input("> ")

    if choice == "naruto":
        print "Great! Do you want fat pikachu to help you?"

        choice = raw_input ("> ")

        if choice == "yes":
            print "I see you read the manga."
            print "Naruto was never able to defeat fat pikachu. Believe it!"
            print "Congrats! You killed him, you monster."
            win()
        elif choice == "no":
            lose()
        else:
            dead("You're not playing the game, god dammit!")
    elif choice == "whatever":
        dead("Clearly you don't care enough to be alive. Goodbye!")
    else:
        print "I have no idea what you said."

def win():
    print "You won!"
    print "Do you go on or revive him by fighting the cthulhu"

    choice = raw_input("> ")

    if choice == "go on":
        dead("Sakura killed you.")
    elif choice == "cthulhu":
        cthulhu()
    else:
        daed("Sakura killed you.")

def lose():
    print "You lost!"
    die("You sit there and die")

def cthulhu():
    print "This is the Cthulhu room."
    print "Do you poke him or ninjustsu at him?"

    choice = raw_input("> ")

    # choice doesn't matter in this if-else statement
    if choice == "poke":
        bear()
    else:
        bear()

def bear():
    print "You won! Cthulhu really is weak."
    print "Look! A bear!"
    print "Your choices are hug her, stab her, marry her, or run away."

    choice = raw_input("> ")

    if choice == "hug":
        cthulhu()
    elif choice == "stab":
        cthulhu()
    elif choice == "marry":
        cthulhu()
    elif choice == "run":
        cthulhu()
    elif choice == "give honey":
        gold()
    else:
        animu()

def gold():
    print "You've entered the gold room"
    print "You win!"
    print "Press enter to live happily ever after"

    choice = raw_input("> ")

    if choice == "This is not real":
        matrix_edn()
    else:
        exit(0)

def blk_hl():
    print "This is the black hole room."
    print "You can go in it if you want."

    choice = raw_input("> ")

    if choice == "in":
        dead_esc("Why would you do that?!")
    else:
        start()

def dead_esc(why):
    print why, "Alright then. Are you just gonna stand there?"

    choice = raw_input("")

    if choice == "yes":
        matrix_edn("I see you played Mario 64. You've been transported.")
    elif choice == "no":
        dead("Seriously, Why would you walk further into a black hole")
    else:
        dead("You clearly don't care.")

def dead(why):
    print why, "You're dead, mate. Good job!"
    exit(0)

def start():
    print "You wake up in a bright, white room."
    print "You see you have three options."
    print "Do you choose to open door one, door two, or do nothing?"

    choice = raw_input ("> ")

    if choice == "door one":
        doorone()
    elif choice == "door two":
        doortwo()
    elif choice == "nothing":
        dead()
    elif choice == "wake up":
        cthulhu_alt()
    else:
        print "Congrats!"
        print "You've found the black hole by doing literally anything else."
        blk_hl()

start()
