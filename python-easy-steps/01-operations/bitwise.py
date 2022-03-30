a, b = 10, 5

print('\nVariables:')
print('a =', a, '\tb =', b)

# OR bitwise operation
# Returns a 1 in each bit where either of two compared bits is a 1
a = a | b
print('\nOR bitwise:')
print('a =', a, '\tb =', b)

# AND bitwise operation
# Returns a 1 in each bit where both of two compared bits is a 1
a, b = 10, 5
a = a & b
print('\nAND bitwise:')
print('a =', a, '\tb =', b)

# NOT bitwise operation
# Returns a 1 in each bit where neither of two compared bits is a 1
a, b = 10, 5
a = ~a
b = ~b
print('\nNOT bitwise:')
print('a =', a, '\tb =', b)

# XOR bitwise operation
# Returns a 1 in each bit where only one of two compared bits is a 1
a, b = 10, 5
a = a ^ b
print('\nXOR bitwise:')
print('a =', a, '\tb =', b)

# Shift Left bitwise operation
# Move each bit that is a 1 a specified number of bits to the left
a, b = 10, 5
a = a << b
print('\nShift Left bitwise:')
print('a =', a, '\tb =', b)

# Shift Right bitwise operation
# Move each bit that is a 1 a specified number of bits to the right
a, b = 10, 5
a = a >> b
print('\nShift Right bitwise:')
print('a =', a, '\tb =', b)
