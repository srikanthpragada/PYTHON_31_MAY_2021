# Returns the first string with largest length
def lengthy_string(*values):
    biggest = values[0]
    for s in values[1:]:
        if len(s) > len(biggest):
            biggest = s

    return biggest


print(lengthy_string('abc', 'xy', 'pqrs', 'defd'))
