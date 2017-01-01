# with-as statement
with open("test.txt", "r+") as file:
    print "What do you want the \"test.txt\" file to say using with-as?"
    content = raw_input("> ")
    file.write(content)
    print file.read()


# Assert
waffles = not(True and False)

assert waffles
# uncommenting code below will throw assertion error
#assert not waffles, "Wrong"


# This uses break and <>
i = 0

while i <> 1:
    print "i =", i
    if i == 10:
        break
    i += 2


# This uses continue in a for loop and a while loop and output equally
for x in range(0, 15):
    print "x =", x
    if x < 9:
        continue
    print "continue was not activated"

x = 0

# x < 14 because when it is 13 it will run loop and print "x = 14"
# so output will be equal to the for-loop above
while x < 14:
    x += 1
    print "x =", x
    if x < 9:
        continue
    print "continue was not activated"



# This is the "String Escape Sequences" part
print "\nString escape sequences!\n"
print """This text\'s is actually, a \"sentence\" that should be grammatically
correct\\errorless,\n\t however I believe that this sentence is boring."""

""" "\b" is backspace, "\r" removes everything before it, "\a" causes a "bell"/
sound to be emmitted by the computer """
# Powershell doesn't show the effects of "\f", "\v"
# "\f" forces the printer to do a page break
# "\v" creates vertical tab 'A vertical tab is set at every multiple of 6 lines'
print "This sente\rnce, \fhowever, is\a p\berfect and int\verensting."



# This is the "string format" part
print "\nString formats!\n"
s = "%d %i %o %u %x %X %e %E %f %F %g %G %c %r %s %g%%"
print s % (45, 77, 10, 909, 1090, 1090, .0000000012, .012, 44, 44, 26562,
 265626, 32, int, 'hell', 55.5)
# newer format function introcuced in 2.6
s = 'I love {0} and {1}, she loves {0} and {1}'
print s.format("apples", "oranges")
# newer format function introcuced in 2.6
s = "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15}"
print s.format(45, 77, 10, 909, 1090, 1090, .0000000012, .012, 44, 44,
26562, 265626, 32, int, 'hell', 55.5)
