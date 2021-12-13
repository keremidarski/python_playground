import time

today = time.strftime("%A")

if today == 'Friday':
    print(f'It is Friday!')
else:
    print(f'It is not Friday ;( Today is {today}.')