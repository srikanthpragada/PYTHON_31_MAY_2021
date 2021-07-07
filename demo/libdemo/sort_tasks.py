from datetime import *

tasks = []
f = open("tasks.txt", "rt")
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:  # Not enough data
        continue

    try:
        startdate = datetime.strptime(parts[1], "%d-%m-%Y")
    except:
        continue  # Startdate is invalid

    if len(parts) == 2:
        msg = "Ongoing"
    else:
        try:
            enddate = datetime.strptime(parts[2], "%d-%m-%Y")
        except:
            continue  # end date is invalid

        days = (enddate - startdate).days
        msg = f"Completed in {days} day(s)"

    tasks.append((parts[0], startdate, msg))

f.close()

# Sort list based on start date (2nd element in tuple)
for task in sorted(tasks, key=lambda t: t[1]):
    stdate = task[1].strftime("%d-%m-%Y")
    print(f"{task[0]:50} {stdate:10}  {task[2]}")
