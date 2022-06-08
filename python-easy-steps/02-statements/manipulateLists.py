basket = ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']


print('\nBasket List:\t\t', basket)
print('No of Basket items:\t', len(basket))
print('\nCrate List:\t\t\t', crate)
print('No of crates items:\t', len(crate))
print('\nTotal number of items:', len(basket) + len(crate))
print('\n------------------------------------')

# Appends an item to the end of the list
print('\nAppend an item to the list:')
basket.append('Damson')
basket_count = len(basket)
print('Added:\t\t\t\t', basket[basket_count - 1])
print('New Basket List:\t', basket)
print('\n------------------------------------')

# Adds all items to the end of the list
print('\nExtend the list:')
basket.extend(crate)
print('Crate list to be added:\t', crate)
print('New Extended basket:\t', basket)
print('\n------------------------------------')

# Inserts item at an indexed position
print('\nInsert an item at pos: 2')
basket.insert(2, 'Strawberries')
basket_count = len(basket)
print('Added:\t\t\t\t', basket[basket_count - 6])
print('New Basket List:\t', basket)
print('\n------------------------------------')

# Remove last item from the list
print('\nRemove the last item from the basket')
print('Last item removed:\t', basket.pop())
print('Basket List:\t\t', basket)
print('\n------------------------------------')

# Remove an item form the list using an index
print('\nRemove an item at pos: 2')
print('Specified item removed:\t', basket.pop(2))
print('Basket List:\t\t\t', basket)
print('\n------------------------------------')

# Returns index position of specified item
print('\nReturns a specified item by string')
print('Specified item located at pos\t', basket.index('Cola')+1)
print('Basket List:\t\t\t\t\t', basket)
print('\n------------------------------------')

# Return the amount of times one specified item is in the list
print('\nReturns a count of a specified item')
print('How many times does BUN appear', basket.count('Bun'))
print('\n------------------------------------')

# Sorts all list items
print('\nSorts the list')
basket.sort()
print(basket)
print('\n------------------------------------')

# Reverse all list items
print('\nReverses the list')
basket.reverse()
print(basket)
print('\n------------------------------------')

# Reset the program
print('\nReset the list')
del basket[3::]
print('Crate list removed:\t', crate)
print('Basket List:\t\t', basket)
