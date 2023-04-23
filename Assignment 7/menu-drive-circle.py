import tkinter as tk
from math import pi

def calculate_area():
    try:
        radius = float(entry.get())
        area = pi * radius ** 2
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        result_label.config(text="Invalid input!")

def calculate_circumference():
    try:
        radius = float(entry.get())
        circumference = 2 * pi * radius
        result_label.config(text=f"Circumference: {circumference:.2f}")
    except ValueError:
        result_label.config(text="Invalid input!")

def exit_program():
    root.destroy()

def area_menu():
    entry.pack()
    calculate_area_button.pack()

def circumference_menu():
    entry.pack()
    calculate_circumference_button.pack()

root = tk.Tk()
root.title("Circle Calculator")

entry = tk.Entry(root)

menu_bar = tk.Menu(root)

circle_menu = tk.Menu(menu_bar, tearoff=0)
circle_menu.add_command(label="Area", command=area_menu)
circle_menu.add_command(label="Circumference", command=circumference_menu)
circle_menu.add_separator()
circle_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="Circle", menu=circle_menu)

root.config(menu=menu_bar)

calculate_area_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_circumference_button = tk.Button(root, text="Calculate Circumference", command=calculate_circumference)
result_label = tk.Label(root, text="")

calculate_area_button.pack_forget()
calculate_circumference_button.pack_forget()
result_label.pack()

root.mainloop()
