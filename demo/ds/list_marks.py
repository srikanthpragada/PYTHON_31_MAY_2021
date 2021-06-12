students = {}

while True:
    data = input("Enter details [end to stop] :")  # name,marks
    if data == "end":
        break
    name, marks = data.split(",")
    students[name] = marks

for name,marks in sorted(students.items()):
    print(f"{name:20} {marks:3}")


