import sys, keyword

print('\nPython version:\t\t\t\t', sys.version)
print('Python interpreter location:', sys.executable)
print('\nPython Module search path:')
for directory in sys.path:
    print('*', directory)

print('\nPython keywords:')
for word in keyword.kwlist:
    print('*', word)
