cities  = {'CA': 'San Francisco', 'MT': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

city_item = cities.items()
print city_item


#ok pay attention
cities['_find'] = find_city

while True:
    print "State? (ENTER to quit)",
    state = raw_input("> ")
    if not state: break

# this line is the most important ever! study!
    city_found  = cities['_find'](cities,state)
    print city_found

for item in cities:
    print item
for item in cities.items():
    print item
