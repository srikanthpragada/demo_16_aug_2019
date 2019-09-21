import sqlite3

con = sqlite3.connect(r"e:\classroom\python\aug16\hr.db")
cur = con.cursor()
# take input
id = input("Enter job  id     :")

cur.execute("delete from jobs where id = ?",(id,))

if cur.rowcount == 1:
    print("Deleted Successfully!")
    con.commit()
else:
    print("Sorry! Invalid Job Id!")

con.close()
