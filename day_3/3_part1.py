# Advent of Code 2021
# Day 3
# Part 1
# @Fabio Birnegger 2021

with open('day3_input.txt') as f:
    data = [x for x in f.read().split()]


def calc_power_consumption(l):
    epsilon = ""
    gamma = ""
    for b in range(len(l[0])):
        zero = 0
        one = 0
        for c in range(len(l)):
            if l[c][b] == '0':
                zero += 1
            else:
                one += 1
        if zero > one:
            gamma += '0'
            epsilon += '1'

        else:
            gamma += '1'
            epsilon += '0'

    g = int(gamma, 2)
    e = int(epsilon, 2)
    answer = g * e
    return answer


print("AOC Day 3 - Part 1 solution:")
print(calc_power_consumption(data))












