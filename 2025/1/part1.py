lines = open(0).read().splitlines()
start = 50
password = 0
for line in lines:
    dir = line[0]
    amount = int(line[1:])
    if dir == 'L':
        start -= amount
    elif dir == 'R':
        start += amount
    start %= 100
    if start == 0:
        password += 1
print(password)
