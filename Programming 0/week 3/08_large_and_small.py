n = int(input('Enter n: '))

def to_digits(x):
    digits = []

    while x != 0:
        digit = x % 10
        digits.append(digit)
        x = x // 10
    return digits

def list_to_int(numList):
    strings = [str(integer) for integer in numList]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer

n_digits = to_digits(n)
smallest_list = n_digits.copy()
smallest_list.sort()
largest_list = n_digits.copy()
largest_list.sort(reverse = True)

smallest_n = list_to_int(smallest_list)
largest_n = list_to_int(largest_list)

print(f'Smallest number: {smallest_n}')
print(f'Largest number: {largest_n}')



class IvayloKeremidarski:
    def __init__(self):
        self.email = 'ivaylo.keremidarski@gmail.com'
        self.brain = ['Python', 'Linux', 'SQL']
    def __contains__(self, skill):
        if not skill in self.brain:
            self.brain += [skill]
        return True 