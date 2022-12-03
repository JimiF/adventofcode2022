#!/usr/bin/python3

sum_priorities = 0

with open('input.txt') as input_file:
    for bag in input_file:
        pocket1, pocket2 = bag[:len(bag)//2], bag[len(bag)//2:]
        
        for item in pocket1:
            if item in pocket2:
                duplicate = item
                break
        
        char_val = ord(duplicate)
        if char_val <= 90:
            priority = char_val - 38
        else:
            priority = char_val - 96
    
        sum_priorities += priority

print(sum_priorities)