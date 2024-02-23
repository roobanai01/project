from tkinter import *

import mysql.connector

con=mysql.connector.connect(

    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_rooban"
)

mycursor = con.cursor()

sql = "INSERT INTO bright_academy (sno,name,sports,products,quantity) VALUES (%s,%s,%s,%s,%s)"
val = ['7','Vinu','Baseball','Baseball','6']
mycursor.execute(sql,val)

con.commit()

print(mycursor.rowcount, "record inserted.")
'''print(con)
result=con.cursor()

sql = "INSERT INTO bright_academy (sno,name,sports,products,quantity) VALUES (%d,%s,%s,%s,%d)"
val = (1,"Rooban","Cricket","Bat",20)
result.execute(sql, val)

con.commit()

print(result.rowcount, "record inserted.")'''

'''sql=Tk()
sql.title("www.Managementportal.com")
sql.geometry("500x500")'''
