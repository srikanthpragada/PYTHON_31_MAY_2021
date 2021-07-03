import os

count = 0
allfiles = os.walk(r"c:\classroom\may31\demo")

for (dirname, folders, files) in allfiles:
    pythonfiles = list(filter(lambda f: f.endswith(".py"), files))
    count += len(pythonfiles)

print("No. of python files = ", count)
