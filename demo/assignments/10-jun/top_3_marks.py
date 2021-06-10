
marks = []
while True:
    num = int(input("Enter marks [-1 to stop] :"))
    if num == -1:
        break
    marks.append(num)

for m in sorted(marks, reverse=True)[:3]:
    print(m)