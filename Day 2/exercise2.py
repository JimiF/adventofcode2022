#!/usr/bin/python3

score = 0

score_table = {
    ('A', 'X'): 3 + 0,
    ('A', 'Y'): 1 + 3,
    ('A', 'Z'): 6 + 2,
    ('B', 'X'): 1 + 0,
    ('B', 'Y'): 2 + 3,
    ('B', 'Z'): 3 + 6,
    ('C', 'X'): 2 + 0,
    ('C', 'Y'): 3 + 3,
    ('C', 'Z'): 1 + 6
}

games = []

with open('input.txt') as input_file:
    for line in input_file:
        line = line.removesuffix("\n")
        line = line.split(" ")
        games.append((line[0], line[1]))

score = sum([score_table[game] for game in games])

print("Score: " + str(score))