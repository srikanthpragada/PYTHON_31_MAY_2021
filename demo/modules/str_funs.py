# String functions

def has_upper(st):
    for c in st:
        if c.isupper():
            return True

    return False


def count_upper(st):
    """
    Returns number of uppercase letters in the given string.
    :param st: String in which we count uppercase letters
    :return: Count of uppercase letters
    """
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


if __name__ == '__main__':   # Invoking it as script
    print("Running String Functions V 1.0")
else:   # Importing it
    print("Importing String Functions V 1.0")
