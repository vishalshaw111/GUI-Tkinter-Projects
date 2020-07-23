from tkinter import *

root=Tk()
root.geometry("1350x750")
root.resizable(0,0)
root.title("TIC-TAC-TOE")
root.configure(background="Cadet Blue")

playerx=IntVar()
playero=IntVar()

playerx.set(0)
playero.set(0)

button=StringVar()
click=True

def checker(button):
    global click
    if button["text"]=="" and click == True:
        button["text"]="X"
        click=False
        check = scorekeeper()
        if (check == 1):
            playerx.set(playerx.get() + 1)
            down = Label(top, text="X WINS", font=('arial', 30, 'bold'), bg="Cadet Blue", padx=350)
            down.grid(row=3, column=0)



    elif button["text"]=="" and click == False:
        button["text"]="O"
        click=True
        check=scorekeeper()
        if check == 2:
            playero.set(playero.get()+1)
            down = Label(top, text="O WINS", font=('arial', 30, 'bold'), bg="Cadet Blue", padx=350)
            down.grid(row=3, column=0)


def reset():
    button1["text"] = ""
    button2["text"] = ""
    button3["text"] = ""
    button4["text"] = ""
    button5["text"] = ""
    button6["text"] = ""
    button7["text"] = ""
    button8["text"] = ""
    button9["text"] = ""

    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")
    down = Label(top, text="", font=('arial', 30, 'bold'), bg="Cadet Blue", padx=350)
    down.grid(row=3, column=0)


def new_game():
    reset()
    playero.set(0)
    playerx.set(0)

def scorekeeper():
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" ):
        button1.configure(background="green")
        button2.configure(background="green")
        button3.configure(background="green")
        return 1

    if (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
        button4.configure(background="green")
        button5.configure(background="green")
        button6.configure(background="green")
        return 1


    if (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
        button7.configure(background="green")
        button8.configure(background="green")
        button9.configure(background="green")
        return 1


    if (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"):
        button1.configure(background="green")
        button4.configure(background="green")
        button7.configure(background="green")
        return 1


    if (button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"):
        button2.configure(background="green")
        button5.configure(background="green")
        button8.configure(background="green")
        return 1

    if (button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        button3.configure(background="green")
        button6.configure(background="green")
        button9.configure(background="green")
        return 1

    if (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
        button1.configure(background="green")
        button5.configure(background="green")
        button9.configure(background="green")
        return 1

    if (button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        button3.configure(background="green")
        button5.configure(background="green")
        button7.configure(background="green")
        return 1

    if (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O"):
        button1.configure(background="green")
        button2.configure(background="green")
        button3.configure(background="green")
        return 2

    if (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O"):
        button4.configure(background="green")
        button5.configure(background="green")
        button6.configure(background="green")
        return 2

    if (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O"):
        button7.configure(background="green")
        button8.configure(background="green")
        button9.configure(background="green")
        return 2


    if (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O"):
        button1.configure(background="green")
        button4.configure(background="green")
        button7.configure(background="green")
        return 2

    if (button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O"):
        button2.configure(background="green")
        button5.configure(background="green")
        button8.configure(background="green")
        return 2

    if (button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        button3.configure(background="green")
        button6.configure(background="green")
        button9.configure(background="green")
        return 2

    if (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"):
        button1.configure(background="green")
        button5.configure(background="green")
        button9.configure(background="green")
        return 2

    if (button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        button3.configure(background="green")
        button5.configure(background="green")
        button7.configure(background="green")
        return 2





top=Frame(root,bg="Cadet Blue",pady=2,width=1350,height=100,relief=RIDGE)
top.grid(row=0,column=0)



top_title=Label(top,text='Tic-Tac-Toe Game',font=('arial', 50 ,'bold'),bd=21,bg="Cadet Blue",fg="Cornsilk",padx=350)
top_title.grid(row=0,column=0)

mainframe=Frame(root,bg="Powder Blue",bd=10,width=1350,height=600,relief=RIDGE)
mainframe.grid(row=1,column=0)

leftframe=Frame(mainframe,bd=10,width=750,height=500,bg='Cadet Blue',padx=10,pady=2,relief=RIDGE)
leftframe.pack(side=LEFT)

rightframe=Frame(mainframe,bd=10,width=560,height=500,bg="Cadet Blue",padx=10,pady=2,relief=RIDGE)
rightframe.pack(side=RIGHT)

rightframe1=Frame(rightframe,bd=10,width=560,height=200,padx=10,pady=2,bg="Cadet Blue",relief=RIDGE)
rightframe1.grid(row=0,column=0)

rightframe2=Frame(rightframe,bd=10,width=560,height=200,padx=10,pady=2,bg="Cadet Blue",relief=RIDGE)
rightframe2.grid(row=1,column=0)

button1=Button(leftframe,text="",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2=Button(leftframe,text="",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3=Button(leftframe,text="",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4=Button(leftframe,text="",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5=Button(leftframe,text="",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6=Button(leftframe,text="",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7=Button(leftframe,text="",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8=Button(leftframe,text="",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9=Button(leftframe,text="",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)


label_playerx=Label(rightframe1,text='Player X:',font=('arial', 40 ,'bold'),bg="Cadet Blue",fg="Cornsilk",padx=2,pady=2)
label_playerx.grid(row=0,column=0,sticky=W)
text_playerx=Entry(rightframe1,bd=2,font=('arial', 20 ,'bold'),textvariable=playerx,fg="black",width=14,)
text_playerx.grid(row=0,column=1)

label_playero=Label(rightframe1,text='Player O:',font=('arial', 40 ,'bold'),bg="Cadet Blue",fg="Cornsilk",padx=2,pady=2)
label_playero.grid(row=1,column=0,sticky=W)
text_playero=Entry(rightframe1,bd=2,font=('arial', 20, 'bold'),textvariable=playero,fg="black",width=14,)
text_playero.grid(row=1,column=1)

button_reset=Button(rightframe2,text="Reset",font=('Times 26 bold'),height=2,width=21,bg="gainsboro",command=reset)
button_reset.grid(row=0,column=0,padx=5,pady=5)

button_new=Button(rightframe2,text="New Game",font=('Times 26 bold'),height=2,width=21,bg="gainsboro",command=new_game)
button_new.grid(row=1,column=0,padx=5,pady=5)



root.mainloop()