s = 0
num_digits = 12
for line in open(0):
    digits = list(map(int, list(line.strip())))
    maxi = 0
    end = len(digits) - num_digits
    max_digits = []
    for _ in range(num_digits):
        maxd = -1
        i = maxi
        while i <= end:
            if digits[i] > maxd:
                maxd = digits[i]
                maxi = i
            i += 1
        max_digits += [maxd]
        end += 1
        maxi += 1
    s += int(''.join(map(str, max_digits)))
print(s)
