file = open('example.txt', 'w')

print('File Name:', file.name)
print('File Mode:', file.mode)
print('Readable:', file.readable())
print('Writable:', file.writable())


def get_status(f):
    if not f.closed:
        return 'Open'
    else:
        return 'Closed'


print('File status:', get_status(file))
file.close()
print('File status:', get_status(file))
