lines = open(0).read().strip().splitlines()
tachyons = [0] * len(lines[0])
tachyons[lines[0].index('S')] = 1
splits = 0
for i in range(len(lines) - 1):
    splitter_idxs = []
    for i, char in enumerate(lines[i + 1]):
        if char == '^':
            splitter_idxs.append(i)
    new_tachyons = tachyons[::]
    for idx in splitter_idxs:
        if tachyons[idx] == 1:
            if idx > 0:
                new_tachyons[idx - 1] = 1
            new_tachyons[idx] = 0
            if idx < len(new_tachyons) - 1:
                new_tachyons[idx + 1] = 1
            splits += 1
    tachyons = new_tachyons
print(splits)
