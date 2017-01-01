# formatter equals that string of format characters with "%"
formatter = "%r %r %r %r"

# prints '1, 2, 3, 4' because the numbers go in each '%r' in the original string  
print formatter % (1, 2, 3, 4)
# prints through the same process as above, but instead it uses words/strings
print formatter % ("one", "two", "three", "four")
# prints through the same process as above using True and False instead
print formatter % (True, False, False, True)
# prints... the string of 'formatter' is put into each '%r' so that prints '%r %r %r %r' 4 times
print formatter % (formatter, formatter, formatter, formatter)
# prints what's in the double quotes.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
