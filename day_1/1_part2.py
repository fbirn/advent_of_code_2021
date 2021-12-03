# Advent of Code 2021
# Day 1
# Part 2
# @Fabio Birnegger 2021

report_str = open('day1_input.txt', 'r').readlines()
l1 = list(map(int, report_str))


def count_measure_sums(l):
    count = 0
    for x in range(len(l)-3):
        if l[x+3] > l[x]:
            count += 1

    return count

print(count_measure_sums(l1))

