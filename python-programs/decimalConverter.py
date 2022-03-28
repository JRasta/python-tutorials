a = input('\nEnter a decimal number: ')


# Returns binary value
def rtnbinary(val):
    return '{0:b}'.format(int(val))


# Formats the binary to 8 digits
def fmtbinary(binary):
    x = binary[::-1]  # reverses an array
    while len(x) < 8:
        x += '0'
    binary = x[::-1]  # resets an array
    return binary


# Returns hexadecimal value
def rtnhexadecimal(val):
    hex_int = hex(val)
    hex_str = hex_int[2::].upper()
    return hex_str


# Returns octal value
def rtnoctal(val):
    oct_int = oct(val)
    oct_str = oct_int[2::]
    return oct_str


# Initial binary values
get_binary = rtnbinary(a)

# Display the converted decimal
print('\nDecimal value:\t\t', a)
print('Binary value:\t\t', fmtbinary(get_binary))
print('Hexadecimal value:\t', rtnhexadecimal(int(a)))
print('Octal value:\t\t', rtnoctal(int(a)))
