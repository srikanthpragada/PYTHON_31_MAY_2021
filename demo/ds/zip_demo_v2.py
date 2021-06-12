names = ['Python', 'Java', 'C#', 'TypeScript', 'Ruby']
versions = [3.9, 16, 10]
years = [1991, 1995, 2000, 2010, 2005]

for idx, n in enumerate(names):
    if idx < len(versions):
        v = versions[idx]
    else:
        v = None

    if idx < len(years):
        y = years[idx]
    else:
        y = None

    print(f"{n:20} {v}  {y}")
