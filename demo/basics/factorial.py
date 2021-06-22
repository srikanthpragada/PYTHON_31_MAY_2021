import sys

if len(sys.argv) < 2:
    print("Usage : python factorial.py number ... ")
    exit(0)

for value in sys.argv[1:]:
    num = int(value)
    fact = 1
    for i in range(2, num + 1):
        fact *= i

    print(f"Factorial of {num} is {fact}")
