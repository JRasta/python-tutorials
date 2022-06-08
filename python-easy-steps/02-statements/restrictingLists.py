print('\nInitial tuple + set:')
print('-----------------------------------')

# A user-defined tuple
# Immutable - tuple(s)
zoo = ('Kangaroo', 'Leopard', 'Moose')
print('Tuple:', zoo, '\tLength:', len(zoo))
print(type(zoo))

# A user-defined set
# Restricted to unique values
bag = {'Red', 'Green', 'Blue'}
print('\nSet:', bag, '\t\t\t\tLength:', len(bag))
print(type(bag))
print('-----------------------------------')

print('\nSet methods:')
print('-----------------------------------')

# Adds item x to the set
print('Add item x to the set')
# code
print('-----------------------------------')

# Adds multiple items to the set
print('Adds multiple items to the set')
# code
print('-----------------------------------')

# Returns a copy of the set
print('Returns a copy of the set')
# code
print('-----------------------------------')

# Removes a random item from the set
print('Removes a random item from the set')
# code
print('-----------------------------------')

# Removes item x if found in the set
print('Removes item x if found in the set')
# code
print('-----------------------------------')

# Returns items that appear in both sets
print('Removes item x if found in the set')
# code
print('-----------------------------------')

# Check if item exists in the set
print('\nIs Green in bag Set?:', 'Green' in bag)
print('Is Orange in bag Set?:', 'Orange' in bag)

# Check if item exists in the tuple
print('\nIs Cat in zoo tuple?:', 'Cat' in zoo)
print('Is Moose in zoo tuple?:', 'Moose' in zoo)

box = {'Red', 'Purple', 'Yellow'}
print('\nSet:', box, '\t\tLength', len(box))
print('Common to both Sets:', bag.intersection(box))
