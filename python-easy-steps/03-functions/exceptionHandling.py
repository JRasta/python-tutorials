title = 'Python In Easy Steps'

try:
    print(titel)
except NameError as msg:
    print('\n*', msg)

# Catch Specific Error type
try:
    a = 5
    b = '0'
    print(a + b)
except TypeError as msg:
    print('*', msg)

day = 32

# Raising a custom exception for custom error handling
try:
    if day > 31:
        raise ValueError('Invalid Day number')
except ValueError as msg:
    print('The Program found An', msg)
finally:
    print('But Today Is Beautiful Anyway')
