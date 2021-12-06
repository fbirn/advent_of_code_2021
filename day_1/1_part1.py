# Advent of Code 2021
# Day 1
# Part 1
# @Fabio Birnegger 2021

report_str = open('day1_input.txt', 'r').readlines()
l1 = list(map(int, report_str))


def count_measures(li):
    count = 0
    for a in range(len(li)):
        if li[a - 1] < li[a]:
            count = count + 1
            a = a + 1

    return count


print("AOC Day 1 - Part 1 solution:")
print(count_measures(l1))
