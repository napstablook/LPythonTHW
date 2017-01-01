# means there are 100 cars
cars = 100
# means that four people can fit in a car
space_in_a_car = 4
# there are 30 drivers
drivers = 30
# there are 90 passengers
passengers = 90
# 70 cars because there are only thirty drivers and 100 cars
cars_not_driven = cars - drivers
# 30 cars_driven b/c there are only 30 drivers to drive the cars
cars_driven = drivers
# output is 120 b/c that's is the potential given the num. of drivers and the space
carpool_capacity = cars_driven * space_in_a_car
# outputs 3 b/c passengers (90) per cars_driven (30) makes 3. So 3 passengers per cars_driven
average_passengers_per_car = passengers / cars_driven


# prints number of cars available
print "There are", cars, "cars available."
# prints number of drivers available
print "There are only", drivers, "drivers available."
# prints number of empty cars
print "There will be",  cars_not_driven, "empty cars today."
# prints number of people that can be transported
print "We can transport", carpool_capacity, "people today."
# prints number of passengers
print "We have", passengers, "to carpool today."
# prints number of average passenger per car
print "We need to put about", average_passengers_per_car, "in each car."
