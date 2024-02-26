from tkinter import *

import mysql.connector

con=mysql.connector.connect(

    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_rooban"
)

rooban = con.cursor()
#for insert option
'''sql = "INSERT INTO bright_academy (sno,name,sports,products,quantity) VALUES (%s,%s,%s,%s,%s)"
val = ['6','Vinu','Baseball','Baseball','10']
rooban.execute(sql,val)

con.commit()

print(rooban.rowcount, "record inserted.")'''
#for delete option
'''sql = "DELETE FROM bright_academy WHERE sno = %s"
val = ['6']
rooban.execute(sql,val)

con.commit()

print(rooban.rowcount, "value deleted.")'''
# for update option
'''sql = "UPDATE bright_academy SET name= %s, sports=%s, products=%s WHERE sno = %s"
val = ['Ragul', 'Throw ball', 'Throwball','5']
rooban.execute(sql,val)

con.commit()

print(rooban.rowcount, "record updated.")'''