# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week7/5-Sandclock

def sand_clock(number):
    og_num = number
    while number > 0:
        star_counter = number
        dot_counter_one = (og_num - star_counter) // 2
        dot_counter_two = (og_num - star_counter) // 2

        while dot_counter_one > 0:

            print('.', end='')
            dot_counter_one -= 1

        while star_counter > 0:

            print('*', end='')
            star_counter -= 1

        while dot_counter_two > 0:

            print('.', end='')
            dot_counter_two -= 1
        print()
        number -= 2

    number += 4

    while number <= og_num:
        star_counter = number
        dot_counter_one = (og_num - star_counter) / 2
        dot_counter_two = (og_num - star_counter) / 2

        while dot_counter_one > 0:

            print('.', end='')
            dot_counter_one -= 1

        while star_counter > 0:

            print('*', end='')
            star_counter -= 1

        while dot_counter_two > 0:

            print('.', end='')
            dot_counter_two -= 1
        print()
        number += 2

sand_clock(5)
