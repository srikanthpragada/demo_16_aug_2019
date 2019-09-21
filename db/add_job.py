import sqlite3

con = sqlite3.connect(r"e:\classroom\python\aug16\hr.db")
cur = con.cursor()
# take input
title = input("Enter job title       :")
minsal = input("Enter min salary      :")
desc = input("Enter job description :")

cur.execute("insert into jobs (title,minsal,description) values(?,?,?)",
            (title, minsal, desc))
print("No. of rows inserted : ", cur.rowcount)

con.commit()
con.close()
