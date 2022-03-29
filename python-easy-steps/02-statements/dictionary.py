print()

diction = {'name': 'Bob', 'ref': 'Python', 'sys': 'Win'}
print('Dictionary:', diction)

print('\nReference', diction['ref'])
print('\nKeys', diction.keys())

del diction['name']
diction['user'] = 'Tom'
print('\nDictionary:', diction)

print('\nIs there a name Key?:', 'name' in diction)
print('Is there a sys Key?:', 'sys' in diction)
