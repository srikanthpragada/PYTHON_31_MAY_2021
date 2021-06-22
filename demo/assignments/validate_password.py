import sys

upper = digit = special = False

pwd = sys.argv[1]
if len(pwd) < 6:
    print("Invalid password!")
    exit()

for c in pwd:
    if c.isupper():
        upper = True
    elif c.isdigit():
        digit = True
    elif c in "@!*":
        special = True

if upper and digit and special:
    print("Valid password!")
else:
    print("Invalid password!")
