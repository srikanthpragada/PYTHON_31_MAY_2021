values = ["abc", "123", "pqr", "a233", "844"]

for n in filter(str.isdigit, values):
    print(n)

for c in filter(str.isupper, "How DO you do"):
    print(c)

# for c in filter(len, "How DO you do"):
#     print(c)
#
# for c in filter(len, ["abc", "", "pqr", "", "a"]):
#     print(c)
