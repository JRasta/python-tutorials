text = 'The political slogan "Workers Of The World Unite!" is from The Communist Manifesto'

with open('manifesto.txt', 'w') as file:
    file.write(text)
    print('\nFile now closed?:', file.closed)

print('File now closed?:', file.closed)

with open('manifesto.txt', 'r+') as file:
    text = file.read()
    print('\nString:', text)
    print('\nPosition in file now:', file.tell())  # Length of the string (chars)
    file.seek(33)
    print('Position in file now:', file.tell())  # Length of the string (chars)
    file.write('All Lands')
    file.seek(59)
    file.write('the tombstone of Karl Marx.')
    file.seek(0)
    text = file.read()
    print('\nString:', text)
