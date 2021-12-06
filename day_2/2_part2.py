# Advent of Code 2021
# Day 2
# Part 2
# @Fabio Birnegger 2021

with open('day2_input.txt') as f:
    data = [x for x in f.read().split('\n')]


def calculate_new_position(l):
    a = 0
    x = 0
    y = 0

    for xx in l:
        xx = xx.split()
        if xx[0] == 'down':
            a += int(xx[1])
        elif xx[0] == 'up':
            a -= int(xx[1])
        else:
            x += int(xx[1])
            y += a * int(xx[1])

    pos = x * y
    return pos


print("AOC Day 2 - Part 2 solution:")
print(calculate_new_position(data))
