num = int(input('Please enter a number: '))

if num > 5:
    print('Number exceeds 5')
elif num < 5:
    print('Number is less than 5')
else:
    print('Number is 5')

if 7 < num < 9:
    print('Number is 8')

if num == 1 or num == 3:
    print('Number is 1 or 3')