import random
import sqlite3

con = sqlite3.connect("ChetNechet.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS ChNch(ChetNechetnost TEXT, num INT)""")
for i in range(100):
    num = random.randint(-100,100)
    if num%2==0:
        cur.execute(f"""INSERT INTO ChNch(ChetNechetnost,Num) values('Чёт','{num}')""")
    else:
        cur.execute(f"""INSERT INTO ChNch(ChetNechetnost,Num) values('Нечёт','{num}')""")

cur.execute("""SELECT * FROM ChNch""")
data = cur.fetchall()
for i in data:
    print(i)

con.close()