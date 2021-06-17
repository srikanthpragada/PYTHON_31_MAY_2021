def upper_lower_count(str):
    ucount = lcount = 0
    for c in str:
        if c.isupper():
            ucount += 1
        elif c.islower():
            lcount += 1

    return (ucount, lcount)   # Tuple


print(upper_lower_count("Abc Xyz Efg!!"))
