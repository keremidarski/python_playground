# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/exam/1-Loss-or-Profit

def loss_or_profit(income, outcome):
    income_sum = sum(income)
    outcome_sum = sum(outcome)

    result = 0
    sign = ''

    if income_sum > outcome_sum:
        result = income_sum - outcome_sum
        sign = '+'
        print(f'{sign}{result}')
    elif income_sum < outcome_sum:
        result = outcome_sum - income_sum
        sign = '-'
        print(f'{sign}{result}')
    else:
        result = 0
        sign = '='
        print(f'{sign}{result}')

loss_or_profit([10], [10])
