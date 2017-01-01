# creates a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


# print "" and gives the function numbers for its variables
print "We can just give the function the numbers directly:"
cheese_and_crackers(20, 30)


# print "" and makes variables with values and places them into the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print "" and gives math to the function using numbers; it gives 30 and 11
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# print "" and gives math to function by using variables and numbers; output 110 and 1050
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)