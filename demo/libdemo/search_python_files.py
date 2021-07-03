import os


def file_contains_string(filename, pattern):
    with open(filename, "rt") as f:
        contents = f.read()
        return pattern in contents


count = 0
allfiles = os.walk(r"c:\classroom\may31\demo")
pattern = input("Enter search string :")

for (dirname, folders, files) in allfiles:
    for file in files:
        filename = dirname + "\\" + file  # Add dirname and filename to get complete path
        if filename.endswith('.py'):
            if file_contains_string(filename, pattern):
                print(filename)
                count += 1

print("No. of python files with search string = ", count)
