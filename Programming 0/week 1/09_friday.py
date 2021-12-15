# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/2-If-Elif-Else-Simple-Problems

import time

today = time.strftime("%A")

if today == 'Friday':
    print(f'It is Friday!')
else:
    print(f'It is not Friday ;( Today is {today}.')
