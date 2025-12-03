ranges = open(0).read().strip().split(',')
answer = 0
for rng in ranges:
    start, end = rng.split('-')
    for number in range(int(start), int(end) + 1):
        as_string = str(number)
        for k in range(1, len(as_string) // 2 + 1):
            if len(as_string) % k != 0:
                continue
            matches = True
            for j in range(k, len(as_string)):
                if as_string[j] != as_string[j % k]:
                    matches = False
            if matches:
                answer += number
                break
print(answer)
