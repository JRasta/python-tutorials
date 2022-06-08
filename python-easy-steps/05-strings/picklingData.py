import os
import pickle

if not os.path.isfile('pickle.dat'):
    data = [0, 1]
    data[0] = input('Enter Topic: ')
    data[1] = input('Enter Series: ')

    file = open('pickle.dat', 'wb')
    pickle.dump(data, file)
    file.close()

    file = open('pickle.dat', 'rb')
    pickle.load(file)
    file.close()

    print('\nWelcome back to:', data[0], data[1])
