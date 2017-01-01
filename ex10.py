tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Study drill 3
moon = "Bright and white."
sun = "brighter and whiter."

print "Link loves the...\n\tMoon."
print "Because it is...\n%s" % moon
print "However, he turns into a wolf at night."
print "So, for now Link loves the...\n\tSun."
print "And it is %s" % sun

# Study drill 4
arrow = "I'm a 'vigi\nlante.\'"
stone = 'I\'m a stone... yeah a stone. I\'m... umm. They call me \'steel.\''

print """
Arrow says, "%r"
Stone says, "%s"
...yep
""" % (arrow, stone)