import math
import random

print('Rounded up 9.5:\t', math.ceil(9.5))
print('Rounded down 9.5:', math.floor(9.5))

num = 4
print(num, 'Squared:\t', math.pow(num, 2))
print(num, 'Square Root:', math.sqrt(num))

nums = random.sample(range(1, 59), 6)
print('Your Lucky Lotto numbers are:', nums)
