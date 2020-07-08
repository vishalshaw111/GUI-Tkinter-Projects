from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
import webbrowser

root=Tk()
root.geometry("800x600")
root.configure(background="black")
root.title("Untitled-Notepad")
root.wm_iconbitmap("notepad.ico")

text=Text(root,font="lucida 10 bold",fg="black",bg="peach puff",undo=TRUE)
file=None
text.pack(fill=BOTH,expand=True)
scroll = Scrollbar(text)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

def new():
    global file
    root.title("Untitled-Notepad")
    file=None
    text.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())
        f.close()

def save_as():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
    else:
        f=open(file,"w")
        f.write(text.get(1.0, END))
        f.close()

def exit():
    root.quit()
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))
def delete():
    text.event_generate(("<<Clear>>"))
def undo():
    text.event_generate("<<Undo>>")
def redo():
    text.event_generate("<<Redo>>")
def callback(url):
    webbrowser.open_new(url)

def about():
    showinfo("About-Notepad","This Notepad has been created by Vishal Shaw,on 7th of december 2019.")

menubar=Menu(root)
menufile=Menu(menubar,tearoff=0)
menufile.add_command(label="New",font="lucida 8 bold",command=new)
menufile.add_command(label="Open",font="lucida 8 bold",command=openfile)
menufile.add_separator()
menufile.add_command(label="Save As",font="lucida 8 bold",command=save_as)
menufile.add_command(label="Exit",font="lucida 8 bold",command=exit)
menubar.add_cascade(label="File",menu=menufile)

menuedit=Menu(menubar,tearoff=0)
menuedit.add_command(label="Undo",font="lucida 8 bold",command=undo)
menuedit.add_command(label="Redo",font="lucida 8 bold",command=redo)
menuedit.add_separator()
menuedit.add_command(label="Cut",font="lucida 8 bold",command=cut)
menuedit.add_command(label="Copy",font="lucida 8 bold",command=copy)
menuedit.add_command(label="Delete",font="lucida 8 bold",command=delete)
menuedit.add_command(label="Paste",font="lucida 8 bold",command=paste)
menubar.add_cascade(label="Edit",menu=menuedit)

#menuview=Menu(menubar,tearoff=0)
#menuview.add_command(label="Zoom_In",font="lucida 8 bold")
#menuview.add_command(label="Zoom_out",font="lucida 8 bold")
#menubar.add_cascade(label="View",menu=menuview)

menuhelp=Menu(menubar,tearoff=0)
menuhelp.add_command(label="View_Help",font="lucida 8 bold",command=lambda : callback("https://www.google.com/search?q=get+help+with+notepad+in+windows+10&rlz=1C1CHBF_enIN870IN870&oq=get+help+in+notepad&aqs=chrome.1.69i57j0j69i60j69i61.11312j0j7&sourceid=chrome&ie=UTF-8"))
menuhelp.add_command(label="About",font="lucida 8 bold",command=about)
menubar.add_cascade(label="Help",menu=menuhelp)
root.config(menu=menubar)


root.mainloop()