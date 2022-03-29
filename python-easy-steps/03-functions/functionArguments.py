def echo(user, lang, sys):
    print('User:', user, 'Lang:', lang, 'System:', sys)


echo('Mike', 'Python', 'Windows')

echo(lang='Python', sys='Mac OS', user='Anne')


def mirror(user='Carole', lang='Python'):
    print('\nUser:', user, 'Lang:', lang)


mirror()
mirror(lang='Java')
mirror(user='Tony')
mirror('Susan', 'C++')
