sqrs = []

for n in range(1, 11):
    sqrs.append(n * n)

print(sqrs)

sqrs2 = [n * n for n in range(1, 11) if n % 2 == 0]
print(sqrs2)
