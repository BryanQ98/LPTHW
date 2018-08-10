#variables
# num of cars
cars = 100
#space available per car
space_in_a_car = 4
#drivers total
drivers = 30
#passengers total
passengers = 90
#cars left not driven
cars_not_driven = cars - drivers
#cars being driven
cars_driven = drivers
#available space to carpool
carpool_capacity = cars_driven * space_in_a_car
#average per car
average_passengers_per_car = passengers / cars_driven

#print those variables within a line of text
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
