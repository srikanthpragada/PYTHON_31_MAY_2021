g = 1000  # Global variable


def f1():
    global g
    g = 10000
    ev = 10  # Enclosing variable

    # Local function
    def f2():
        nonlocal ev
        ev = 0
        lv = 100  # Local variable
        print(lv, ev, g)

    f2()
    print(ev)


f1()
