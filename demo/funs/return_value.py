print(print(10))
print(len('abc'))


def iseven(n):
    return n % 2 == 0


def count_upper(s: str):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


print(iseven(10))
print(count_upper("AbcXyz"))
# print(count_upper(1000))
