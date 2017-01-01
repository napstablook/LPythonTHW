# prints ""
print "Mary had a little lamb."
# prints "" and %s is replaced with 'snow'
print "Its fleece was white as %s." % 'snow'
# prints ""
print "And everywhere that Mary went."
# prints "." (dot) and multiplies it by 10... so ten dots
print "." * 10  # what'd that do?

# from end1-end12 assigns a string/letter to each variable
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# combines strings from end1-end6... which makes "Cheese"... comma makes next print line be outputted on the same line with a space... So "Cheese Burger"
print end1 + end2 + end3 + end4 + end5 + end6,
# combines strings from end7-end12... so output is "Burger"
print end7 + end8 + end9 + end10 + end11 + end12
