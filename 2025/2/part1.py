#!/usr/bin/env pypy3
import re

ranges = open(0).read().replace('\n', '').strip().split(',')
answer = 0
for rng in ranges:
    start, end = rng.split('-')
    for num in range(int(start), int(end)+1):
        if re.search(r'^(\d+)\1$', str(num)):
            answer += num
print(answer)
