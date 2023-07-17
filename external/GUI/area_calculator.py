import tkinter
from tkinter import Entry, Label, Button,messagebox,PhotoImage
import math


def clicked():
    r = int(txt.get())
    area = math.pi*(r**2)
    perimeter = 2*math.pi*r
    res = "Area is: "+str(area)+"Perimeter: "+str(perimeter)
    label.configure(text=res)
    messagebox.showinfo("Message title","Message Content")   #dialog box

window = tkinter.Tk()
window.geometry('500x500')
label1 = Label(window, text="Enter the radius of circle")
txt = Entry(window)
txt.insert(0,0)
button = Button(window, text="Enter", command=clicked)
label = Label(window)
image=PhotoImage(file="bw.gif",width=30,height=30)

label3=Label(window,image=image)
label1.grid(row=0, column=0)
txt.grid(column=0, row=1)
button.grid(row=2, column=0)
label.grid(row=3, column=0)

window.mainloop()
