interval_lower = int(input('Enter lower bound: '))
interval_upper = int(input('Enter upper bound: '))
number = int(input('Enter number: '))

if number == interval_lower:
    print('The number is equal to the lower bound of the interval')
elif number == interval_upper:
    print('The number is equal to the upper bound of the interval')
elif interval_lower < number < interval_upper:
    print('The number is in the interval')
elif number < interval_lower:
    print('The number is outside the interval, x < a')
elif number > interval_upper:
    print('The number is outside the interval, x > b')