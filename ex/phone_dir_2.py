dir = {}

while True:
    name = input("Enter name [end to stop] : ")
    if name == 'end':
        break
    phone = input("Enter phone number : ")
    if name in dir:
        dir[name].add(phone)  # add to existing set
    else:
        dir[name] = {phone}   # create new entry with name and set

for n, p in sorted(dir.items()):
    print(f"{n:15} {','.join(sorted(p))}")
