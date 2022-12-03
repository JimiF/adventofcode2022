#!/usr/bin/python3

sum_priorities = 0

with open('input.txt') as input_file:
    bags = input_file.readlines()
    for x in range(0, len(bags), 3):
        commonitem = list(set(bags[x].rstrip())& set(bags[x+1].rstrip()) & set(bags[x+2].rstrip()))
        char_val = ord(commonitem[0])
        if char_val <= 90:
            priority = char_val - 38
        else:
            priority = char_val - 96
        sum_priorities += priority

print(sum_priorities)