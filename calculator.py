from tkinter import *

root = Tk("Simple Calculator")
root.title=("Simple Calculator")

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
count=0
def b_click(num):
	#e.delete(0,END)
	global count
	e.insert(count,num)
	count+=1

def clrfn():
	e.delete(0,END)	
	
def btn_add():
	n1=e.get()
	global f_num
	global fn
	fn="add"
	f_num=float(n1)
	e.delete(0,END)

def btn_sub():
	n1=e.get()
	global f_num
	global fn
	fn="sub"
	f_num=int(n1)
	e.delete(0,END)

def btn_mul():
	n1=e.get()
	global f_num
	global fn
	fn="mul"
	f_num=float(n1)
	e.delete(0,END)		

def btn_div():
	n1=e.get()
	global f_num
	global fn
	fn="div"
	f_num=float(n1)
	e.delete(0,END)


def equalTo():
	second_number=e.get()
	e.delete(0,END)
	if fn=="add":
		e.insert(0, f_num+float(second_number))
	elif fn=="sub":
		e.insert(0, f_num-float(second_number))
	elif fn=="mul":
		e.insert(0, f_num*float(second_number))
	elif fn=="div":
		e.insert(0, f_num/float(second_number))		
	


b1= Button(root,text="1",padx=40,pady=20,command=lambda: b_click(1))
b2= Button(root,text="2",padx=40,pady=20,command=lambda: b_click(2))
b3= Button(root,text="3",padx=40,pady=20,command=lambda: b_click(3))
b4= Button(root,text="4",padx=40,pady=20,command=lambda: b_click(4))
b5= Button(root,text="5",padx=40,pady=20,command=lambda: b_click(5))
b6= Button(root,text="6",padx=40,pady=20,command=lambda: b_click(6))
b7= Button(root,text="7",padx=40,pady=20,command=lambda: b_click(7))
b8= Button(root,text="8",padx=40,pady=20,command=lambda: b_click(8))
b9= Button(root,text="9",padx=40,pady=20,command=lambda: b_click(9))
b0= Button(root,text="0",padx=40,pady=20,command=lambda: b_click(0))
b_add= Button(root,text="+",padx=39,pady=20,command=btn_add)
b_sub= Button(root,text="-",padx=40,pady=20,command=btn_sub)
b_mul= Button(root,text="*",padx=40,pady=20,command=btn_mul)
b_div= Button(root,text="/",padx=40,pady=20,command=btn_div)
b_equal= Button(root,text="=",padx=90,pady=20,command=equalTo)
b_clear= Button(root,text="clear",padx=79,pady=20,command=clrfn)

b1.grid(row=3 ,column=0)
b2.grid(row=3 ,column=1)
b3.grid(row=3 ,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2 ,column=1)
b6.grid(row=2 ,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1 ,column=1)
b9.grid(row=1 ,column=2)

b0.grid(row=4 ,column=0 )
b_clear.grid(row=4 ,column=1, columnspan=2 )
b_add.grid(row=5 ,column=0 )
b_sub.grid(row=6 ,column=0 )
b_mul.grid(row=6 ,column=1 )
b_div.grid(row=6 ,column=2 )
b_equal.grid(row=5 ,column=1 , columnspan=2)

root.mainloop()