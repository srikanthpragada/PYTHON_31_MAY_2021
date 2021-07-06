from datetime import *

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

    print(f"{parts[0]:50}  {parts[1]:10} {msg}")

f.close()
