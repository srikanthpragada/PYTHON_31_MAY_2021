nums = [123, 345, 150, 855]

digits = set()  # Empty set

for n in nums:
    # digits = digits.union(set(str(n)))
    digits.update(set(str(n)))

for d in sorted(digits):
    print(d)
