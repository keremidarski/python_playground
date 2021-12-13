first_name = input('Enter first name: ')
second_name = input('Enter second name: ')
third_name = input('Enter third name: ')
birth_year = int(input('Enter birt year: '))

person = {}
person['first_name'] = first_name
person['second_name'] = second_name
person['third_name'] = third_name
person['current_age'] = 2021 - birth_year

print(person)