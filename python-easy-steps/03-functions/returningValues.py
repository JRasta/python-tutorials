num = input('Enter an integer: ')


def square(num):
    if num.isdigit():
        num = int(num)
        return num * num
    else:
        return 'Invalid entry'


print(num, 'Squared is:', square(num))
