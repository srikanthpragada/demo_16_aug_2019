import sqlite3

con = sqlite3.connect(r"e:\classroom\python\aug16\hr.db")
cur = con.cursor()
cur.execute("select * from jobs order by minsal desc")

for job in cur.fetchall():
    print(f"{job[1]:20s} {job[2]:10d} {job[3]}")

con.close()