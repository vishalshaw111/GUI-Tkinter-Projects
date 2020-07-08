from tkinter import *

import click as click

root=Tk()
root.geometry("400x500")
root.resizable(0,0)
root.title("MY CALCULATOR")
def click(event):
    global user
    text=event.widget.cget("text")
    if text=="=":
        if user.get().isdigit():
            value=int(user.get())
        else:
            value=eval(userentry.get())
        user.set(value)
    elif text=="C":
        user.set("")

    else:
        user.set(user.get()+text)

user=StringVar()
user.set("")
f=Frame(root)
f.pack(expand=True,fill=BOTH)
userentry=Entry(f,textvariable=user,font="comicsansms 20 bold",relief=SUNKEN,borderwidth=20)
userentry.pack(expand=True,fill=BOTH)
f1=Frame(root,bg="red")
f1.pack(expand=True,fill=BOTH)
f2=Frame(root,bg="black")
f2.pack(expand=True,fill=BOTH)
f3=Frame(root,bg="pink")
f3.pack(expand=True,fill=BOTH)
f4=Frame(root,bg="orange")
f4.pack(expand=True,fill=BOTH)

b=Button(f1,text="1",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f1,text="2",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f1,text="3",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f1,text="+",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f2,text="4",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f2,text="5",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f2,text="6",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f2,text="-",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f3,text="7",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f3,text="8",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f3,text="9",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f3,text="*",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f4,text="0",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f4,text="C",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f4,text="=",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)

b=Button(f4,text="/",relief=SUNKEN,bg="cyan",borderwidth=20,font="comicsansms 20 bold")
b.pack(side=LEFT,expand=True,fill=BOTH)
b.bind("<Button-1>", click)



root.mainloop()

