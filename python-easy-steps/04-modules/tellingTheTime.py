from datetime import *

today = datetime.today()
print('Today is:', today, '\n')

for attr in \
['year', 'month', 'day', 'hour', 'minute', 'second']:
    print(attr, ':\t', getattr(today, attr))

print('\nTime: ', today.hour, ':', today.minute, sep='')

day = today.strftime('%A')
month = today.strftime('%B')

print('Date:', day, month, today.day)
