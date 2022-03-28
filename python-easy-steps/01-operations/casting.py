a = input('\nEnter a number: ')
b = input('Now enter another number: ')

total = a + b
print('\nData Type sum:', total, type(total))
total = int(a) + int(b)
print('Data Type sum:', total, type(total))
total = float(total)
print('Data Type sum:', total, type(total))
total = chr(int(total))
print('Data Type sum:', total, type(total))
