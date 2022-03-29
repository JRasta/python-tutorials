chars = ['A', 'B', 'C']
fruit = ('Apple', 'Banana', 'Cherry')
diction = {'name': 'Mike', 'ref': 'Python', 'sys': 'Win'}

print('\nElements:\t', end='')
for item in chars:
    print(item, end='')

print('\nEnumerated:\t', end='')
for item in enumerate(chars):
    print(item, end='')

print('\nZipped:\t', end='')
for item in zip(chars, fruit):
    print(item, end='')

print('\nPaired')
for key, value in diction.items():
    print(key, '=', value)
