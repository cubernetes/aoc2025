a, b = open(0).read().split('\n\n')
fresh = []
for line in a.splitlines():
    s, e = line.split('-')
    fresh += [[int(s), int(e) + 1]]
t = 0
seen = set()
for line in b.splitlines():
    for f in fresh:
        if int(line) in range(f[0], f[1]):
            if line not in seen:
                t += 1
                seen.add(line)
print(t)
