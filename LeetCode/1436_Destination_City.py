# Problem description:
# https://leetcode.com/problems/destination-city/

def dest_city(paths):
    outgoing_count = {}

    for path in paths:
        city_a, city_b = path
        outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
        outgoing_count[city_b] = outgoing_count.get(city_b, 0)

    for city in outgoing_count:
        if outgoing_count[city] == 0:
            return city
        
# Expected: 'Sao Paulo'
print(dest_city([['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']]))
# Expected: 'A'
print(dest_city([["B","C"],["D","B"],["C","A"]]))
