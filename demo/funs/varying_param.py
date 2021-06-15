def wish(*names, message="Hello"):
    for n in names:
        print("Hello", n)


wish("Bill", "Larry", message="Hi")
wish("Bill", "Larry", "Tim", "Mark")
