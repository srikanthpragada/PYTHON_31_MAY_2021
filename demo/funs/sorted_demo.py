nums = [-10, 10, 4, 5, -6, -7]
langs = ["Java", "Python", "C", "C++", "Cobol", "JavaScript"]
names = [" java", "  Python", "C", " C++", "cobol", "    JavaScript"]


def convert_string(s):
    return s.strip().upper()


# for n in sorted(nums, key=abs):
#     print(n)


for n in sorted(langs, key=len):
    print(n)

for n in sorted(names, key=convert_string):
    print(n.strip())
