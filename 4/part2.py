lines = list(map(list, open(0).read().splitlines()))

def remove() -> int:
    global lines
    total = 0

    # mark cells to be removed with y
    for i in range(len(lines)):
        for j in range(len(lines)):
            adj = 0
            for off_i, off_j in [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]:
                if 0 <= i + off_i < len(lines) and 0 <= j + off_j < len(lines):
                    if lines[i + off_i][j + off_j] in '@y':
                        adj += 1
            if adj < 4 and lines[i][j] == '@':
                total += 1
                lines[i][j] = 'y'
    for line in lines:
        print(''.join([y if y != 'y' else '\033[31m@\033[m' for y in line]))
    print()

    # remove cells marked with y
    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] == 'y':
                lines[i][j] = 'x'
    return total

prev_removed=-1
total = 0
for line in lines:
    print(''.join(line))
print()
while True:
    removed = remove()
    if removed == 0:
        break
    print('Removed', removed, 'rolls of paper')
    prev_removed = removed
    total += removed
print(total)
