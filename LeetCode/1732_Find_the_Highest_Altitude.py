# Problem description:
# https://leetcode.com/problems/find-the-highest-altitude/

def highest_altitude(gain):
    altitude = 0
    max_altitude = 0

    for i in gain:
        altitude += i

        if altitude > max_altitude:
            max_altitude = altitude

    return max_altitude

# Expected: 0
print(highest_altitude([-4, -3, -2, -1, 4, 3, 2]))
