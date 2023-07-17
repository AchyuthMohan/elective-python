import tkinter
from tkinter import PhotoImage,Label

window=tkinter.Tk()
window.geometry("300x300")
image=PhotoImage(file="bw.gif")
label=Label(window,image=image)
label.grid(row=0,column=0)
window.mainloop()
