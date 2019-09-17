from datetime import datetime

f = open("players.txt","rt")
players = {}
cd = datetime.now()   # current date
for line in f:
    parts = line.strip("\n").split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    try:
        dob = datetime.strptime(parts[1],"%d-%m-%Y")
        years = (cd - dob).days // 365
        players[name] = years
    except:
        pass


f.close()

for  name,age in sorted(players.items(), key = lambda t : t[1]):
    print(f"{name:20} {age}")





