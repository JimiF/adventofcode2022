#!/usr/bin/python3

elves = []
value = 0
with open('input.txt') as input_file:
    for line in input_file:
        if line in ["\n", "\r\n"]:
            elves.append(int(value))
            value = 0
        else:
            value += int(line)


print("Elf Number: " + str(elves.index(max(elves))+1))
print("Calories: " + str(max(elves)))