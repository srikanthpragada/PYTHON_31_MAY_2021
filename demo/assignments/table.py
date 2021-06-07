num = int(input("Enter number :"))

for i in range(1, 11):
    # print(f"{num:3} * {i:3} = {num * i:5}")
    print("%3d * %3d = %5d" % (num, i, num * i))

