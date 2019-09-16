import re

f = open("persons.txt")
p1 = re.compile("[a-zA-Z ]+")  # Name
p2 = re.compile(r"\d{5,}")     # Phone

people = {}

for line in f:
    name = p1.search(line)
    if name is None:
        continue

    phone = p2.search(line)
    if phone is None:
        continue

    people[name.group().strip()] = phone.group()

f.close()

for n,p in sorted(people.items()):
    print(f"{n:20} {p}")
