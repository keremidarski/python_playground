def gas_stations(distance, tank_size, stations):
    result = []
    traveled = 0
    index = 0
    gas = tank_size
    last_station = 0

    while index < len(stations) and traveled + gas < distance:
        if stations[index] < traveled + gas:
            last_station = stations[index]
            gas -= stations[index] - traveled
            traveled = stations[index]
            index += 1
        else:
            if last_station + tank_size < stations[index]:
                return result
            else:
                result.append(last_station)
                gas = tank_size
    
    if last_station > 0 and last_station not in result:
        result.append(last_station)
    return result

tests = [
    ((320, 90, [50, 80, 140, 180, 220, 290]), [80, 140, 220, 290]),
    ((390, 80, [70, 90, 140, 210, 240, 280, 350]), [70, 140, 210, 280, 350]),
    ((100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]), [40, 80]),
    ((100, 101, [200]), []),
    ((100, 50, [200]), []),
    ((100, 50, [10, 90]), []),
]

for args, expected in tests:
    result = gas_stations(*args)

    passing = result == expected

    if passing:
        print(passing)
    else:
        print(passing, result)