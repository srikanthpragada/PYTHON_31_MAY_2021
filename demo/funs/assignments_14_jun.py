def table(num, len=10):
    for i in range(1, len + 1):
        print(num, i, num * i)


def common_factors(n1, n2, /):
    s = n1 if n1 < n2 else n2
    for i in range(2, s // 2 + 1):
        if n1 % i == 0 and n2 % i == 0:
            print(i)


table(15, 5)
common_factors(255, 125)
