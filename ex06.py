# makes x equal what is inside the quotes and %d will be replaced by 10 when printed
x = "There are %d types of people." % 10
# binary equals the string "binary"
binary = "binary"
# do_not equals the string "don't"
do_not = "don't"
# y equals the string "" and %s's are replaced with the values of binary and do_not when y is called
y = "Those who know %s and those who %s." % (binary, do_not)

# prints x value (string)
print x
# prints y value (string)
print y

# prints "" and replaces %r with x which is a string
print "I said: %r." % x
# prints "" and puts y value on '%s'
print "I also said: '%s'." % y

# hilarious equals False
hilarious = False
# joke_evaluation equals "" and contains %r which can call something else
joke_evaluation = "Isn't that joke so funny?! %r"

# prints joke_evaluation and assigns hilarious to %r because of the % (percent) sign
print joke_evaluation % hilarious

# w equals the string
w = "This is the left side of..."
# e equals the string
e = "a string with a right side."

# prints w and/plus e strings
print w + e
