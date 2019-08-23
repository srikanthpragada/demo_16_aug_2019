dir = {}

while True:
    name = input("Enter name [end to stop] : ")
    if name == 'end':
        break
    phone = input("Enter phone number : ")
    dir[name] = phone

for n, p in sorted(dir.items()):
    print(f"{n:15} {p}")
