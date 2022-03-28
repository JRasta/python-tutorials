basket = ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']

print('\nBasket List:\t\t', basket)
print('No of Basket items:\t', len(basket))
print('------------------------------------')

basket.append('Damson')
basket_count = len(basket)
print('\nAdded:\t\t\t\t', basket[basket_count - 1])
print('Basket List:\t\t', basket)

print('\nLast item removed:\t', basket.pop())
print('Basket List:\t\t', basket)
print('No of Basket items:\t', len(basket))
print('------------------------------------')

basket.extend(crate)
print('\nCrate list added:\t', crate)
print('Extended basket:\t', basket)

del basket[3::]
print('\nCrate list removed:\t', crate)
print('Basket List:\t\t', basket)
