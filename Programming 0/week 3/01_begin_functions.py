# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week3/1-Baby-Steps

def square(x):
    return x ** 2

#print(square(5))

def fact(x):
    start = 1
    product = 1

    while start <= x:
        product *= start
        start += 1
    
    return product

#print(fact(6))

def count_elements(x):
    counter = 0

    for i in x:
        counter += 1
    
    return counter

#print(count_elements(['ivo', 'jeko', 'edi']))

def member(x, xs):
    is_member = True

    if x not in xs:
        is_member = False
    
    return is_member

#print(member('Python', ['Django', 'Rails']))

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]

def grades_that_pass(students, grades, limit):
    result = []
    for count, value in enumerate(grades):
        if value >= limit:
            result += [students[count]]           
    
    return result

#print(grades_that_pass(students, grades, 4.0))
