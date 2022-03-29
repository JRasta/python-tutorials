for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 1:
            print('Breaks inner loop at i = 2 j = 1')
            # Used to break a loop when a specified condition is met
            break

        if i == 1 and j == 1:
            print('Continues inner loop at i = 1 j = 1')
            # Used to skip a single iteration of a loop
            continue

        print('Running i =', i, 'j =', j)
