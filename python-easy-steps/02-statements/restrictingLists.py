# A user-defined tuple
zoo = ('Kangaroo', 'Leopard', 'Moose')
print('Tuple:', zoo, '\tLength:', len(zoo))
print(type(zoo))

# A user-defined set
bag = {'Red', 'Green', 'Blue'}
bag.add('Yellow')
print('\nSet:', bag, '\tLength:', len(bag))
print(type(bag))

print('\nIs Green in bag Set?:', 'Green' in bag)
print('Is Orange in bag Set?:', 'Orange' in bag)

print('\nIs Cat in zoo tuple?:', 'Cat' in zoo)
print('Is Moose in zoo tuple?:', 'Moose' in zoo)

box = {'Red', 'Purple', 'Yellow'}
print('\nSet:', box, '\t\tLength', len(box))
print('Common to both Sets:', bag.intersection(box))
