#!/usr/bin/python3

import heapq

elves = []
value = 0
with open('input.txt') as input_file:
    for line in input_file:
        if line in ["\n", "\r\n"]:
            elves.append(int(value))
            value = 0
        else:
            value += int(line)

top_three_elves = heapq.nlargest(3, elves)      
print("Total Calories: " + str(sum(top_three_elves)))