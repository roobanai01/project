from tkinter import *
import os
win=Tk()
win.title("www.personaldetails.com")
win.geometry("500x500+500+500")
win.state("zoomed")

def createTitle():
    titleImageFrame=Frame(win,width=600,height=400, bg="white")
    titleImageFrame.pack()

    imgdir=os.path.join(os.path.dirname(__file__),'img')
    print("Path name is : " + imgdir)

    imageloction=os.path.join(imgdir,'welcome.gif')
    print("image location is : " + imageloction)

    titleimage=PhotoImage("titleimg",file=os.path.join(imgdir,"welcome.gif"))


    lblTitleImage=Label(titleImageFrame, image=titleimage)
    lblTitleImage.pack()


def login():
    a=tbEntrya.get()
    b=tbEntryb.get()
    if(a=="rooban") & (b=="1234"):
        print("You are enterd....")
    else:
        print("You are not allowed....")


label1msg=Label(win,text="User Name",font=("Batang",14),fg="black")
label1msg.grid(row=1,column=20,pady=10)
tbEntrya=Entry(win, width=60)
tbEntrya.grid(row=1,column=25)

label1msg=Label(win,text="Password",font=("Batang",14),fg="black")
label1msg.grid(row=2,column=20,pady=10)
tbEntryb=Entry(win, width=60)
tbEntryb.grid(row=2,column=25)

btnlo=Button(win,text="Login",font=("Batang",14),fg="White",bg="Green",command=login)
btnlo.grid(row=7,column=1)

win.mainloop()