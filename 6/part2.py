import numpy as np
import re
lines = list(map(list, open(0).read().strip().splitlines()))
longest = -1
for line in lines:
    if len(line) > longest:
        longest = len(line)
lines[-1] = list((''.join(lines[-1])).ljust(longest))
lines = re.sub(r'\n *\n', r'\n\n', '\n'.join([''.join(x) for x in np.transpose(lines)]))
problems = [x.splitlines() for x in lines.split('\n\n')]
total = 0
for prob in problems:
    first = prob[0]
    other = prob[1:]
    op = first[-1]
    result = first[:-1]
    result = int(result)
    for num in other:
        if op == '*':
            result *= int(num)
        elif op == '+':
            result += int(num)
        else:
            assert False
    total += result
print(total)
