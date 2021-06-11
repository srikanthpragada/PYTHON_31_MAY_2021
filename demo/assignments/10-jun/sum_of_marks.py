data = "89,76,55,69,,87,abc,45"

marks = data.split(",")
total = 0
for v in marks:
    if v.isdigit():
       total += int(v)

print(total)
