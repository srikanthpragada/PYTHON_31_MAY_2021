import os

sourcefile = "names.txt"
targetfile = "temp.txt"

with open(sourcefile, "rt") as source, open(targetfile, "wt") as target:
    for line in source:
        line = line.strip()
        if len(line) > 0:  # if not blank line
            target.write(line + "\n")

# remove source
os.remove(sourcefile)
os.rename(targetfile, sourcefile)
