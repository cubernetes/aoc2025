#!/usr/bin/env pypy3

lines = open(0).read().splitlines()
pos = 50
password = 0
for line in lines:
    dir = line[0]
    amount = int(line[1:])
    if dir == 'L':
        for _ in range(amount):
            pos -= 1
            pos %= 100
            if pos == 0:
                password += 1
    elif dir == 'R':
        for _ in range(amount):
            pos += 1
            pos %= 100
            if pos == 0:
                password += 1
    pos %= 100
print(password)
