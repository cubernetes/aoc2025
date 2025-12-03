#!/usr/bin/env pypy3

s = 0
for line in open(0):
    digits = list(map(int, list(line.strip())))

    max_digits = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
    for md_i, _md in enumerate(max_digits):
        end = -(len(max_digits)-md_i-1)
        if end == 0:
            end = len(digits)
        initial_offset = max_digits[md_i-1 if md_i-1 >= 0 else 0][1] + 1
        for idx, digit in enumerate(digits[max_digits[md_i-1 if md_i-1 >= 0 else 0][1] + 1:end]):
            if digit > max_digits[md_i][0]:
                max_digits[md_i][0] = digit
                max_digits[md_i][1] = idx + initial_offset
    s += int(''.join(list(map(lambda tup: str(tup[0]), max_digits))))
print(s)
