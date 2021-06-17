nums = [10, -20, 0, 34, 55]


def ispositive(n):
    return n > 0


for n in filter(ispositive, nums):
    print(n)
