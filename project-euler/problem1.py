# Project Euler - Problem 01

# If we list all the natural numbers below 10 that are multiples of 3 or 5
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Author: J. Smith
# Date: 28/03/2022

multiples = []
i = 1
a = 0

while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)
    i += 1

for x in multiples:
    a += x

print('Multiples of 3 & 5 below 1000:', multiples)
print('Total of the multiples:\t', a)
