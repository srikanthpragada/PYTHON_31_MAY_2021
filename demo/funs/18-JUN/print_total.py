# Program to consider 0 if any of the strings cannot be converted to float

nums = ["200", "100", "42.64", ".38383", "abdgdd", "xyz", "2345sdgjns"]
total = 0


def convert_float(s):
    for c in s:
        if not (c.isdigit() or c == '.'):
            return 0

    return float(s)


total = sum(map(convert_float, nums))

print("The total is", total)
