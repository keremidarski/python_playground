# https://leetcode.com/problems/destination-city/

# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
# Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

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
