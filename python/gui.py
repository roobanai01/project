from tkinter import *
win=Tk()
win.title("Mathematical Operations")
win.geometry("500x500+500+500")
win.state("zoomed")

def Addition():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a+b
    labeloutput.config(text=c)
def Subtraction():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a-b
    labeloutput.config(text=c)
def Multiplication():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a*b
    labeloutput.config(text=c)
def Division():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a/b
    labeloutput.config(text=c)

Labeltitle=Label(win,text="Arithematic Operations",font=("ALGERIAN",16),fg="green")
Labeltitle.grid(row=0,column=20)

label1msg=Label(win,text="Enter the Value of A",font=("Lucida Calligraphy",14),fg="blue")
label1msg.grid(row=1,column=20,pady=20)
tbEntrya=Entry(win, width=60)
tbEntrya.grid(row=1,column=25)

label2msg=Label(win,text="Enter the Value of B",font=("Lucida Calligraphy",14),fg="blue")
label2msg.grid(row=2,column=20,pady=20)
tbEntryb=Entry(win, width=60)
tbEntryb.grid(row=2,column=25)

labeloutput=Label(win,text=" ")
labeloutput.grid(row=3,column=30,pady=20)


btnadd=Button(win,text="Addition",font=("calibri",14),fg="White",bg="Black",command=Addition)
btnadd.grid(row=5,column=1)

btnsub=Button(win,text="Subtraction",font=("calibri",14),fg="White",bg="Black",command=Subtraction)
btnsub.grid(row=5,column=2)

btnmul=Button(win,text="Multiplication",font=("calibri",14),fg="White",bg="Black",command=Multiplication)
btnmul.grid(row=5,column=3)

btndiv=Button(win,text="Division",font=("calibri",14),fg="White",bg="Black",command=Division)
btndiv.grid(row=5,column=4)


win.mainloop()
