names = ['Python', 'Java', 'C#']
versions = [3.9, 16, 10]
years = [1991, 1995, 2000]

for idx, name in enumerate(names, start=1):
    print(idx, name)

for idx, name in enumerate(names):
    print(name, versions[idx])
