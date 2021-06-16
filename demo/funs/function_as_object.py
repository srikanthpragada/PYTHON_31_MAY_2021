def wish():
    print("Hello")


print(type(wish))
hwish = wish
print(type(hwish))


def wish(message):
    print(message)


hwish()
wish("Hi")
