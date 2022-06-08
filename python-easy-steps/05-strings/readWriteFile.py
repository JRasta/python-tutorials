poem = 'I never saw a man who looked\n'
poem += 'With such a wistful eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

file = open('poem.txt', 'w')
file.write(poem)
file.close()

file = open('poem.txt', 'r')
for line in file:
    """
    Passing the whitespace to the end parameter (end='') indicates that the end 
    character has to be identified by whitespace and not a newline.
    """
    print(line, end='')
file.close()

file = open('poem.txt', 'a')
file.write('(Oscar Wilde)')
file.close()
