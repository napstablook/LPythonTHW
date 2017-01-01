from sys import argv

script, user_name, of = argv
prompt = 'Answer: '

print "Hi %s of %s, I'm the %s script." % (user_name, of, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where did you live before %s, %s?" % (of, user_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You lived in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)