a, b = open(0).read().split('\n\n')
fresh = []
for line in a.splitlines():
    s, e = line.split('-')
    fresh += [[int(s), int(e)]]

fresh.sort()
t = 0

prev_end = -1
for f in fresh:
    s, e = f
    if s <= prev_end:
        s = prev_end + 1
    if s > e:
        continue
    print(f'Adding range {s} {e}')
    t += e - s + 1
    prev_end = e

print(t)
