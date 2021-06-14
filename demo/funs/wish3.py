def wish(msg="Hello", name="Guest"):
    print(msg, name)


wish()
wish("Good Morning")
wish("Hi", "Mark")

# Keyword arguments
wish(name="Bob", msg="Hi")
wish(msg="Hi")
