from tkinter import *
#import mysql.connector


win=Tk()

win.title("Insert into mysql DB Demo")
win.geometry("500x500")

frameleft=Frame(win,bg="black",width=500,height=500,padx=30,pady=30)
frameleft.pack(side=LEFT)

frameright=Frame(win,bg="red",width=500,height=500,padx=30,pady=30)
frameright.pack(side=RIGHT)

lbl_title_of_operation=Label(frameleft,text="Insert into mysql DB Demo")
lbl_title_of_operation.pack(side=TOP)

lbl_title_of_operation=Label(frameright,text="Insert into mysql DB Demo")
lbl_title_of_operation.pack(side=TOP)

lblName=Label(frameleft,text="Name")
lblName.grid(row=2,column=1,padx=30,pady=10)


win.mainloop()
