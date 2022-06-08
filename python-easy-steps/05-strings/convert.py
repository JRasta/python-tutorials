import unicodedata

# Non ASCII character included
s = 'Ástríðr'

print('\nRed String:', s)
print('Type:', type(s), '\tLength:', len(s))

s = s.encode('utf-8')
print('\nEncoded String:', s)
print('Type:', type(s), '\tLength:', len(s))

s = s.decode('utf-8')
print('\nDecoded String:', s)
print('Type:', type(s), '\tLength:', len(s))
print()

# Print out the correct name of the char
for i in range(len(s)):
    print(s[i], unicodedata.name(s[i]), sep=': ')
