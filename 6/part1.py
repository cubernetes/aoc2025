import numpy as np
lines = np.array([x.split() for x in open(0).read().splitlines()])
lines = np.transpose(lines)
print(lines)
t = 0
for line in lines:
    op = line[-1]
    nums = list(map(int, line[:-1]))
    if op == '+':
        t2 = 0
    else:
        t2 = 1
    for num in nums:
        if op == '+':
            t2 += int(num)
        else:
            t2 *= int(num)
    t += t2
print(t)
