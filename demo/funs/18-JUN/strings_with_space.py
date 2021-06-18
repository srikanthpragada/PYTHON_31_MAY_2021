# Program to use filter to select all strings that contain one or more spaces

values = ["How are you?", "Are you okay?", "Good", "I am fine"]


def has_space(st):
    for c in st:
        if c.isspace():
            return True

    return False


for i in filter(has_space, values):
    print(i)
