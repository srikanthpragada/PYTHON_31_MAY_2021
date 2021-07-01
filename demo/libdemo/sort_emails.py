# Take emails from emails.txt and display them in sorted order

f = open("emails.txt", "rt")
emails = set()
for line in f.readlines():
    parts = line.strip().split(",")
    emails.update(parts)

f.close()

for email in sorted(emails):
    print(email)
