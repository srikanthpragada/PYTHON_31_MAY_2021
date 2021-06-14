
st = "Java"
chars = {}

for idx, c in enumerate(st):
    if c in chars:
        chars[c].append(idx)
    else:
        chars[c] = [idx]


print(chars)