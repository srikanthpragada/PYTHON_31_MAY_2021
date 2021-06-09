s1 = "abcabcxyzabc"
s2 = "zyzabcaabb"

common = []  # Empty list
for c in s1:
    if c in s2 and c not in common:
        common.append(c)

for c in common:
    print(c)
