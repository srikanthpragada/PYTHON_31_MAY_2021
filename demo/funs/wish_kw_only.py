# Keyword-only arguments
def wish(*, msg, name="Guest"):
    print(msg, name)


wish(msg="Good Morning")
wish(name="Mark", msg="Hi")
wish("Hi")
