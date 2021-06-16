# Return a list of strings with largest length
def lengthy_string(*values):
    largest_length = len(values[0])
    for s in values[1:]:
        if len(s) > largest_length:
            largest_length = len(s)

    return [s for s in values if len(s) == largest_length]


print(lengthy_string('abc', 'xy', 'pqrs', 'defd'))
