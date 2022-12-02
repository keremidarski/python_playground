# AOC 2022 Day 01 Puzzle 01

import re


def prep_input():
    dwarfs = []

    with open("input.txt", "r") as f:
        data = re.split("(?<!\.)\n\n", f.read())

    for dwarf in data:
        dwarfs.append([int(cal) for cal in dwarf.split("\n")])

    return dwarfs


def most_calories(dwarfs):
    max_cal = 0

    for dwarf in dwarfs:
        if sum(dwarf) > max_cal:
            max_cal = sum(dwarf)

    return max_cal


def main():
    data = prep_input()
    result = most_calories(data)
    print(result)

    

if __name__ == "__main__":
    main()
