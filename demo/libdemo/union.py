file1 = "names.txt"
file2 = "names2.txt"

with open(file1, "rt") as f1, open(file2, "rt") as f2:
    lines = set(f1.readlines()) | set(f2.readlines())

for line in sorted(lines):
    print(line, end='')
