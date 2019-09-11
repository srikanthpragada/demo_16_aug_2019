f = open("students.txt","rt")

for line in f.readlines():
    parts = line.strip("\n").split(",")
    if len(parts) < 2:   # Ignore line if it doesn't contain data
        continue

    name = parts[0]
    total = 0
    for m in parts[1:]:
        if m.isdigit():
           total += int(m)

    print(f"{name:10} {total}")


f.close()


