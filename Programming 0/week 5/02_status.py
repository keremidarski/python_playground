# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week5/2-Course-Status

def status_count(students):
    finalized = []
    not_finalized = []

    for student in students:
        if student['status'] == 'finalized':
            finalized.append(student['name'])
        elif student['status'] == 'not_finalized':
            not_finalized.append(student['name'])
    
    result = {'finalized': finalized, 'not_finalized': not_finalized}

    return result

students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]

print(status_count(students))
