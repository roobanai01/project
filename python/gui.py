'''from tkinter import *
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


win.mainloop()'''

# Importing Tkinter module 
'''from tkinter import *
from tkinter.ttk import *

# Creating master Tkinter window 
master = Tk() 
master.geometry("175x175") 

# Tkinter string variable 
# able to store any string value 
v = StringVar(master, "1") 

# Dictionary to create multiple buttons 
values = {"RadioButton 1" : "1", 
		"RadioButton 2" : "2", 
		"RadioButton 3" : "3", 
		"RadioButton 4" : "4", 
		"RadioButton 5" : "5"} 

# Loop is used to create multiple Radiobuttons 
# rather than creating each button separately 
for (text, value) in values.items(): 
	Radiobutton(master, text = text, variable = v, 
		value = value).pack(side = TOP, ipady = 5) 

# Infinite loop can be terminated by 
# keyboard or mouse interrupt 
# or by any predefined function (destroy()) 
mainloop()'''




from tkinter import *
win=Tk()
win.title("www.personaldetails.com")
win.geometry("500x500+500+500")
win.state("zoomed")

def Submit():
    a=tbEntrya
    b=tbEntryb
    c=tbEntryc
    d=tbEntryd
    e=tbEntrye
    f=a+b+c+d+e
    labeloutput.config(text=f)


Labeltitle=Label(win,text="Personal Details Form",font=("ALGERIAN",20),fg="Blue")
Labeltitle.grid(row=0,column=25)

label1msg=Label(win,text="Name",font=("Batang",14),fg="black")
label1msg.grid(row=1,column=20,pady=10)
tbEntrya=Entry(win, width=60)
tbEntrya.grid(row=1,column=25)

label2msg=Label(win,text="Gender",font=("Batang",14),fg="black")
label2msg.grid(row=2,column=20,pady=10)
tbEntryb=Entry(win, width=60)
tbEntryb.grid(row=2,column=25)

label3msg=Label(win,text="D.O.B",font=("Batang",14),fg="black")
label3msg.grid(row=3,column=20,pady=10)
tbEntryc=Entry(win, width=60)
tbEntryc.grid(row=3,column=25)

label4msg=Label(win,text="Birth City",font=("Batang",14),fg="black")
label4msg.grid(row=4,column=20,pady=10)
tbEntryd=Entry(win, width=60)
tbEntryd.grid(row=4,column=25)

label5msg=Label(win,text="Phone No.",font=("Batang",14),fg="black")
label5msg.grid(row=5,column=20,pady=10)
tbEntrye=Entry(win, width=60)
tbEntrye.grid(row=5,column=25)

labeloutput=Label(win,text=" ")
labeloutput.grid(row=8,column=30,pady=20)

btnsub=Button(win,text="Submit",font=("Batang",14),fg="White",bg="Green",command=Submit)
btnsub.grid(row=7,column=1)

btnclr=Button(win,text="Clear",font=("Batang",14),fg="White",bg="Blue")
btnclr.grid(row=7,column=2)

btnclo=Button(win,text="Close",font=("Batang",14),fg="White",bg="Red")
btnclo.grid(row=7,column=3)

win.mainloop()