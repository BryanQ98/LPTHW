# create state name to its abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI',
}

# creates set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
}

# add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['NY'])

# print out some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")
	
# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")
	
# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"(state state is abbreviated {abbrev})")
	print(f"and has city {cities[abbrev]}")
	
print('-' * 10)
# get a abbreviation by state that might not be there
state = states.get('Texas')

if not states:
	print("Sorry, no Texas.")
	
# get a city with a default values
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")