studs = {}

while True:
    rollno = int(input("Enter rollno [0 to stop] : "))
    if rollno == 0:
        break
    marks = int(input("Enter marks : "))
    if rollno in studs:
        studs[rollno] += marks
    else:
        studs[rollno] = marks

for r, m in sorted(studs.items()):
    print(f"{r:-10} {m}")
