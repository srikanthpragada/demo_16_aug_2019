import sqlite3

con = sqlite3.connect(r"e:\classroom\python\aug16\hr.db")
cur = con.cursor()
cur.execute("select avg(minsal),min(minsal), max(minsal) from jobs")

avgsal = cur.fetchone()[0]
print(f"Avg. minsal : {avgsal:8.0f}")

con.close()