def change(v):
    print(id(v))
    v = 0
    print(id(v))


def addfirst(lst, value):
    lst.insert(0, value)


a = 100
print(id(a))
change(a)
print(a)

l = [1, 2, 3]
addfirst(l, 4)
print(l)
