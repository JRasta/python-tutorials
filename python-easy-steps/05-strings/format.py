# Common format
snack = '{} and {}'.format('Burger', 'Fries')
print('\nReplaced', snack)

snack = '{1} and {0}'.format('Burger', 'Fries')
print('Replaced', snack)

# Substituted format
snack = '%s and %s' % ('Milk', 'Chocolate')
print('\nSubstituted', snack)
