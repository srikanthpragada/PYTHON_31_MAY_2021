data = "89,76,55,69,,87,45"

marks = data.split(",")
total = 0
for v in marks:
    total += int(v)

print(total)
