# Take 5 numbers or until 0 is given and then display sum of numbers

total = 0
for i in range(5):
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break

    total = total + num

print("Total = ", total)
