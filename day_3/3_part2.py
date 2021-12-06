# Advent of Code 2021
# Day 3
# Part 2
# @Fabio Birnegger 2021


with open('day3_input.txt') as f:
    data = [x for x in f.read().split()]

#Calculate oxygen value
i = 0
while len(data) > 1:
    zero = 0
    one = 0
    onelist = []
    zerolist = []
    for c in range(len(data)):
        if data[c][i] == '0':
            zero += 1
            zerolist.append(data[c])
        else:
            one += 1
            onelist.append(data[c])
    if zero > one:
        data = zerolist
    else:
        data = onelist
    i += 1
oxygen = int(data[0], 2)

# calculate co2 value
with open('day3_input.txt') as f:
    data2 = [x for x in f.read().split()]
i = 0
while len(data2) > 1:
    zero = 0
    one = 0
    onelist = []
    zerolist = []
    for c in range(len(data2)):
        if data2[c][i] == '0':
            zero += 1
            zerolist.append(data2[c])
        else:
            one += 1
            onelist.append(data2[c])
    if one < zero:
        data2 = onelist
    else:
        data2 = zerolist
    i += 1
co2 = int(data2[0], 2)

answer = oxygen * co2
print("AOC Day 3 - Part 2 solution:")
print(answer)
