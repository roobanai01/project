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
from tkinter import ttk
win=Tk()
win.title("www.personaldetails.com")
win.geometry("500x500+500+500")
win.state("zoomed")

def Submit():
    a=tbEntrya.get()
    #b=tbEntryb.get()
    b=combo.get()
    c=tbEntryc.get()
    d=tbEntryd.get()
    e=tbEntrye.get()
    f=tbEntrye.get()
    labeloutput1.config(text=a)
    labeloutput2.config(text=b)
    labeloutput3.config(text=c)
    labeloutput4.config(text=d)
    labeloutput5.config(text=e)
    labeloutput5.config(text=f)
def Clear():
    a=" "
    b=" "
    c=" "
    d=" "
    e=" "
    f=" "
    labeloutput1.config(text=a)
    labeloutput2.config(text=b)
    labeloutput3.config(text=c)
    labeloutput4.config(text=d)
    labeloutput5.config(text=e)
    labeloutput5.config(text=f)
def option_selected(event):
   selected_option = combo.get()

def optionselected(event):
   selected_option = combo2.get()

def optionselected(event):
   selected_option = combo3.get()

Labeltitle=Label(win,text="Personal Details Form",font=("ALGERIAN",20),fg="White",bg="Blue")
Labeltitle.grid(row=0,column=25)

label1msg=Label(win,text="Name",font=("Batang",14),fg="black")
label1msg.grid(row=1,column=20,pady=10)
tbEntrya=Entry(win, width=60)
tbEntrya.grid(row=1,column=25)

'''label2msg=Label(win,text="Gender",font=("Batang",14),fg="black")
label2msg.grid(row=2,column=20,pady=10)
tbEntryb=Entry(win, width=60)
tbEntryb.grid(row=2,column=25)'''

label2msg=Label(win,text="Gender",font=("Batang",14),fg="black")
label2msg.grid(row=2,column=20,pady=10)
combo=ttk.Combobox(win,values=["Male","Female","Others"])
combo.grid(row=2,column=25,pady=10)

label3msg=Label(win,text="D.O.B",font=("Batang",14),fg="black")
label3msg.grid(row=3,column=20,pady=10)
tbEntryc=Entry(win, width=60)
tbEntryc.grid(row=3,column=25)

label4msg=Label(win,text="Birth City",font=("Batang",14),fg="black")
label4msg.grid(row=4,column=20,pady=10)
'''tbEntryd=Entry(win, width=60)
tbEntryd.grid(row=4,column=25)'''
combo2=ttk.Combobox(win,values=["Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Erode", "Kanchipuram", "Kanyakumari", "Karur", "Krishnagiri", "Madurai", "Nagapattinam", "Namakkal", "Perambalur", "Pudukkottai", "Ramanathapuram", "Salem", "Sivaganga", "Thanjavur", "The Nilgiris", "Theni", "Thoothukudi", "Tiruchirapalli", "Tirunelveli", "Tiruvallur", "Tiruvannamalai", "Tiruvarur", "Vellore", "Viluppuram", "Virudhunagar"])
combo2.grid(row=4,column=25)
label5msg=Label(win,text="State",font=("Batang",14),fg="black")
label5msg.grid(row=5,column=20,pady=10)
#tbEntryd=Entry(win, width=60)
#tbEntryd.grid(row=5,column=25)
combo3=ttk.Combobox(win,values=["Andaman & Nicobar Island","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra & Nagar Haveli","Daman & Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"])
combo3.grid(row=5,column=25)

label6msg=Label(win,text="Phone No.",font=("Batang",14),fg="black")
label6msg.grid(row=6,column=20,pady=10)
tbEntrye=Entry(win, width=60)
tbEntrye.grid(row=6,column=25)

labeloutput1=Label(win,text=" ")
labeloutput1.grid(row=8,column=30,pady=15)
labeloutput2=Label(win,text=" ")
labeloutput2.grid(row=9,column=30,pady=15)
labeloutput3=Label(win,text=" ")
labeloutput3.grid(row=10,column=30,pady=15)
labeloutput4=Label(win,text=" ")
labeloutput4.grid(row=11,column=30,pady=15)
labeloutput5=Label(win,text=" ")
labeloutput5.grid(row=12,column=30,pady=15)

btnsub=Button(win,text="Submit",font=("Batang",14),fg="White",bg="Green",command=Submit)
btnsub.grid(row=7,column=1)

btnclr=Button(win,text="Clear",font=("Batang",14),fg="White",bg="Blue", command=Clear)
btnclr.grid(row=7,column=2)

btnclo=Button(win,text="Close",font=("Batang",14),fg="White",bg="Red")
btnclo.grid(row=7,column=3)

win.mainloop()