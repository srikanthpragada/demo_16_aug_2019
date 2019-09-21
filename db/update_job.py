import sqlite3

con = sqlite3.connect(r"e:\classroom\python\aug16\hr.db")
cur = con.cursor()
# take input
id = input("Enter job  id     :")
desc = input("Enter job description :")

cur.execute("update jobs set description = ? where id = ?",(desc,id))
if cur.rowcount == 1:
    print("Updated Successfully!")
    con.commit()
else:
    print("Sorry! Invalid Job Id!")

con.close()
