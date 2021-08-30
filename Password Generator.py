from tkinter import *
import  random,string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")

title = StringVar()
label = Label(root,textvariable = title,font= ('Helvetica 15 underline')).pack()
title.set("The Length of Password")

def selection():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value = 1,fg = "Red",pady= 20,padx = 20,width = 40,command=selection).pack(anchor = CENTER)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value = 2,fg = "Blue",pady= 20,padx = 20,width = 40,command=selection).pack(anchor = CENTER)
R3 = Radiobutton(root, text="ADVANCE", variable=choice,value = 3,fg = "grey",pady= 20,padx = 20,width = 40,command=selection).pack(anchor = CENTER)
labelchoice = Label(root)
labelchoice.pack()

lenlable = StringVar()
lenlable.set("Password Length")
lentittle = Label(root,textvariable=lenlable,pady= 20,padx = 20,width = 40,).pack()

val = IntVar()
spinelength = Spinbox(root, from_=8,to_=24,textvariable = val,width = 40, ).pack()

def callback():
    Isum.config(text = passgen())

passgenButton = Button(root,text=" Click Me To Get Your Password", command=callback,pady= 20,padx = 20,width = 40,).pack(anchor = CENTER)
password = str(callback)

Isum = Label(root,text="")
Isum.pack(side = BOTTOM)

var = StringVar()
label = Label( root, textvariable=var,bg = "red" )

var.set("Hey!? How are you doing? Here is your Password. Thanks for using This")
label.pack()

poor = string.ascii_uppercase+string.ascii_lowercase
average = string.ascii_lowercase+string.ascii_uppercase+string.digits
symbols = """~!@#$%^&*()=[]{}\/><?"""
Advance = poor+average+symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average,val.get()))
    else:
        return "".join(random.sample(Advance,val.get()))

root.mainloop()
