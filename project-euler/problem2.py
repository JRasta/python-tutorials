# Project Euler - Problem 02

# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

# Author: J. Smith
# Date: 28/03/2022

total = 0
i = 0
fib = 0
fib2 = 1


while i < 10:

    total = fib + fib2
    fib = fib2
    fib2 = total
    i += 1
    print(total)

print('\nFinished')
