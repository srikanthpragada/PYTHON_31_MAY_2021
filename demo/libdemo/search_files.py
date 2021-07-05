# python search_files.py searchstring startdir

import os
import sys

if len(sys.argv) < 2:
    print("Usage : python search_files.py searchstring [startdir] ")
    exit(0)

if len(sys.argv) == 2:   # Start directory is not given
    startdir = os.getcwd()
else:
    startdir = sys.argv[2]

searchstring = sys.argv[1]
count = 0
allfiles = os.walk(startdir)

for (dirname, folders, files) in allfiles:
    for f in files:
        if searchstring in f:
            print(dirname + "\\" + f)
            count += 1

print("No. of files found = ", count)
