import sqlite3

f = open("jobs.csv", "rt")
con = sqlite3.connect(r"e:\classroom\python\aug16\hr.db")
cur = con.cursor()

for line in f:
    parts = line.strip("\n").split(",")
    if len(parts) < 3:
        continue

    try:
        cur.execute("insert into jobs (title,minsal,description) values(?,?,?)",
                    (parts[0], parts[1], parts[2]))
    except Exception as ex:
        pass

f.close()
con.commit()
con.close()
