marks = [84, 56, 77, 78, 90, 80, 80]

sorted_marks = sorted(marks, reverse=True)
for m in sorted_marks[:3]:
    print(m)

pos = 3
while sorted_marks[2] == sorted_marks[pos]:
    print(sorted_marks[pos])
    pos += 1
