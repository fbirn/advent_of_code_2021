# Advent of Code 2021
# Day 2
# Part 1
# @Fabio Birnegger 2021

with open('day2_input.txt') as f:
    data = [x for x in f.read().split("\n")]


def calculate_position(l):
    x = 0
    y = 0
    for xx in l:
        xx = xx.split()
        if xx[0] == 'forward':
            x += int(xx[1])
        elif xx[0] == 'down':
            y += int(xx[1])
        else:
            y -= int(xx[1])

    multpos = x * y
    return multpos


print("AOC Day 2 - Part 1 solution:")
print(calculate_position(data))

