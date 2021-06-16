def print_details(*args, **kwargs):
    for v in args:
        print(v)

    for k, v in kwargs.items():
        print(k, v)


print_details(x=10, y=20, r=30, name='Abc')
print_details(a=10, b=20)
print_details(10, 20, a=1, b=2)
