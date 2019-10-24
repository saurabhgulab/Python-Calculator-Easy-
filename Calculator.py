from tkinter import*

def onclick(num):
    global symbol
    symbol=symbol+str(num)
    tf.set(symbol)
def clear():
    global symbol
    tf.set("")
def equals():
    global symbol
    total=str(eval(symbol))
    tf.set(total)
    symbol=""

B=Tk()
B.title("Saurabh's Calculator")
symbol=""
tf=StringVar()
Result=Entry(B,font=("ariel",30,"bold"),bd=25,insertwidth=4,bg="white",justify="right",fg="black",textvariable=tf)
Result.grid(columnspan=4)
#first-row
B1=Button(B,text='A',font=("ariel",25,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=20,command=clear)
B1.grid(row=1,column=0)
B1=Button(B,text='+/-',font=("ariel",20,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=20,command=lambda:onclick('+/-'))
B1.grid(row=1,column=1)
B1=Button(B,text='%',font=("ariel",20,"bold"),bg="gray",fg="white",bd=10,padx=25,pady=20,command=lambda:onclick('%'))
B1.grid(row=1,column=2)
B1=Button(B,text='÷',font=("ariel",20,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=20,command=lambda:onclick('÷'))
B1.grid(row=1,column=3)

B1=Button(B,text='7',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(7))
B1.grid(row=2,column=0)
B1=Button(B,text='8',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(8))
B1.grid(row=2,column=1)
B1=Button(B,text='9',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(9))
B1.grid(row=2,column=2)
B1=Button(B,text='x',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick('x'))
B1.grid(row=2,column=3)

B1=Button(B,text='4',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(4))
B1.grid(row=3,column=0)
B1=Button(B,text='5',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(5))
B1.grid(row=3,column=1)
B1=Button(B,text='6',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(6))
B1.grid(row=3,column=2)
B1=Button(B,text='-',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick('-'))
B1.grid(row=3,column=3)

B1=Button(B,text='1',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(1))
B1.grid(row=4,column=0)
B1=Button(B,text='2',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(2))
B1.grid(row=4,column=1)
B1=Button(B,text='3',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(3))
B1.grid(row=4,column=2)
B1=Button(B,text='+',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick('+'))
B1.grid(row=4,column=3)

B1=Button(B,text='0',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(0))
B1.grid(row=5,column=0)
B1=Button(B,text='C',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick('C'))
B1.grid(row=5,column=1)
B1=Button(B,text='.',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=lambda:onclick(''))
B1.grid(row=5,column=2)
B1=Button(B,text='=',font=("ariel",30,"bold"),bg="gray",fg="white",bd=10,padx=20,pady=10,command=equals)
B1.grid(row=5,column=3)
B.mainloop()

