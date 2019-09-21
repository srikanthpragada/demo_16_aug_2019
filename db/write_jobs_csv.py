import sqlite3


f = open("jobs.csv","wt")
con = sqlite3.connect(r"e:\classroom\python\aug16\hr.db")
cur = con.cursor()
cur.execute("select * from jobs order by id")

for job in cur.fetchall():
    f.write(f"{job[0]},{job[1]},{job[2]},{job[3]}\n")

con.close()
f.close()

