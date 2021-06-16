def common_factors(*numbers):
    smallest = min(numbers)
    for n in range(2, smallest // 2 + 1):
        for v in numbers:
            if v % n != 0:
                break
        else:
            print(n)


def get_common_factors(*numbers):
    smallest = min(numbers)
    factors = []
    for n in range(2, smallest // 2 + 1):
        for v in numbers:
            if v % n != 0:
                break
        else:
            factors.append(n)

    return factors


common_factors(10, 20, 50)
print(get_common_factors(30, 60))
