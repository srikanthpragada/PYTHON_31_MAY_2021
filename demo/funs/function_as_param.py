def math_operation(a, b, operation):
    result = operation(a, b)
    print(result)


def add(x, y):
    return x + y


def multiply(n1, n2):
    return n1 * n2


def square(n):
    return n * n


math_operation(10, 20, add)
math_operation(10, 20, multiply)
# math_operation(9, 10, square)
