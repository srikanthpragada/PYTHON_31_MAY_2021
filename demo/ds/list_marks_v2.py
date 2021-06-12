students = {}
details = ["Joe,90", "Bob,87", "Mike,88", "Bill,76"]

for data in details:
    name, marks = data.split(",")
    students[name] = marks

for name, marks in sorted(students.items()):
    print(f"{name:20} {marks:3}")
