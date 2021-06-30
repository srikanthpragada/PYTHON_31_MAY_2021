def numbers(maximum):
    for i in range(1, maximum + 1):
        yield i


g = numbers(5)
print(type(g))
print(next(g))
print(next(g))