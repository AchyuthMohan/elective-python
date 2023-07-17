import tkinter
from tkinter import Label, Button,Entry,Checkbutton,BooleanVar
flag=0
def clicked():
    res="Hello "+txt.get()
    label.configure(text=res)
    print("Button was clicked..")
    print(check_state.get())
window = tkinter.Tk()

window.title('GUI')

window.geometry("300x300")

# widgets
label = Label(window,text="Please enter ur name")
txt=Entry(window,width=10)
button=Button(text="Enter", command=clicked, fg="red",bg='yellow')

check_state=BooleanVar()
check_state.set(False)
chk=Checkbutton(window,text="check me",var=check_state)

# grids
label.grid(column=0, row=0)
button.grid(column=1, row=0)
txt.grid(column=0,row=2)
chk.grid(row=3,column=0)

window.mainloop()
