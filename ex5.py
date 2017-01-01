name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # inchest convert to centimeters
weight = 180 * 0.45359237 # lbs convert to kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r centimeters tall." % height
print "He's %r kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %s, %s, and %s I get %s." % (
	age, height, weight, age + height + weight)