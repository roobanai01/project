'''from tkinter import *
master = Tk()
w= Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y=int(canvas_height/2)
w.create_line(0,y,canvas_width,y)
mainloop()'''

'''from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='Kaasi',variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='Kalai',variable=var2).grid(row=1, sticky=W)
mainloop()'''

'''from tkinter import *
master = Tk()
Label (master, text='FirstName').grid(row=0)
Label (master, text='LastName').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()'''

'''from tkinter import *
top = Tk()
Lb=Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'React JS')
Lb.insert(5, 'Any other')
Lb.pack()
top.mainloop()'''


'''print("**** This program is copyrighted to Rooban ****")
from tkinter import *
expression = "" 
def press(num): 	
	global expression 
	expression = expression + str(num)	
	equation.set(expression)

def equalpress():	
	try: 
		global expression		
		total = str(eval(expression))
		equation.set(total)		
		expression = "" 	
	except: 

		equation.set(" error ") 
		expression = "" 



def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


 
if __name__ == "__main__": 
	
	gui = Tk() 

	
	gui.configure(background="light green") 

	
	gui.title("Simple Calculator") 

	
	gui.geometry("270x150") 

	
	equation = StringVar() 

	
	expression_field = Entry(gui, textvariable=equation) 

	
	expression_field.grid(columnspan=4, ipadx=70)

	button1 = Button(gui, text=' 1 ', fg='black', bg='red', 
					command=lambda: press(1), height=1, width=7) 
	button1.grid(row=2, column=0) 

	button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
					command=lambda: press(2), height=1, width=7) 
	button2.grid(row=2, column=1) 

	button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
					command=lambda: press(3), height=1, width=7) 
	button3.grid(row=2, column=2) 

	button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
					command=lambda: press(4), height=1, width=7) 
	button4.grid(row=3, column=0) 

	button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
					command=lambda: press(5), height=1, width=7) 
	button5.grid(row=3, column=1) 

	button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
					command=lambda: press(6), height=1, width=7) 
	button6.grid(row=3, column=2) 

	button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
					command=lambda: press(7), height=1, width=7) 
	button7.grid(row=4, column=0) 

	button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
					command=lambda: press(8), height=1, width=7) 
	button8.grid(row=4, column=1) 

	button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
					command=lambda: press(9), height=1, width=7) 
	button9.grid(row=4, column=2) 

	button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
					command=lambda: press(0), height=1, width=7) 
	button0.grid(row=5, column=0) 

	plus = Button(gui, text=' + ', fg='black', bg='red', 
				command=lambda: press("+"), height=1, width=7) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='red', 
				command=lambda: press("-"), height=1, width=7) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='red', 
					command=lambda: press("*"), height=1, width=7) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='red', 
					command=lambda: press("/"), height=1, width=7) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='red', 
				command=equalpress, height=1, width=7) 
	equal.grid(row=5, column=2) 

	clear = Button(gui, text='Clear', fg='black', bg='red', 
				command=clear, height=1, width=7) 
	clear.grid(row=5, column='1') 

	Decimal= Button(gui, text='.', fg='black', bg='red', 
					command=lambda: press('.'), height=1, width=7) 
	Decimal.grid(row=6, column=0) 
	
	gui.mainloop()'''

from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
def show():
    num=askinteger("input","input an Integer")
    print(num)
B=
