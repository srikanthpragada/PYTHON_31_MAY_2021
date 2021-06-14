details = ["Joe,90,80,76", "Bob,87,87", "Mike,88,,45,67", "Bill,76,74,89"]
students = {}
for data in details:
    name, *input_marks = data.split(",")
    marks = [int(v) for v in input_marks if v.isdigit()]
    students[name] = sum(marks)

for name, total in sorted(students.items()):
    print(f"{name:10} {total:3}")
