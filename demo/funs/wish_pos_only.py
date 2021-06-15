# Positional-only arguments
def wish(msg, name="Guest", /):
    print(msg, name)


wish("Good Morning")
wish("Hi", "Mark")
# wish(msg="Hello")
