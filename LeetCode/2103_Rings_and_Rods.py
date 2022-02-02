# Problem description:
# https://leetcode.com/problems/rings-and-rods/

def count_points(rings):
    ring_colors = {}
    result = 0

    for i in range(0, len(rings), 2):
        if rings[i + 1] not in ring_colors:
            ring_colors[rings[i + 1]] = rings[i]
        else:
            ring_colors[rings[i + 1]] += rings[i]

    for value in ring_colors.values():
        if 'R' in value and 'G' in value and 'B' in value:
            result += 1

    return result

print(count_points("B0B6G0R6R0R6G9"))