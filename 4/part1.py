lines = list(map(list, open(0).read().splitlines()))
total = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        adj = 0
        for off_i, off_j in [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]:
            if 0 <= i + off_i < len(lines) and 0 <= j + off_j < len(lines):
                if lines[i + off_i][j + off_j] in '@x':
                    adj += 1
        if adj < 4 and lines[i][j] == '@':
            total += 1
            lines[i][j] = 'x'
for line in lines:
    print(line)
print(total)
