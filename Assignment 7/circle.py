import tkinter as tk
from math import pi
def calculate_area():
    radius = float(entry.get())
    area = pi * radius ** 2
    result_label.config(text=f"Area: {area:.2f}")
def calculate_circumference():
    radius = float(entry.get())
    circumference = 2 * pi * radius
    result_label.config(text=f"Circumference: {circumference:.2f}")
root = tk.Tk()
root.title("Circle Calculator")
entry = tk.Entry(root)
entry.pack()
area_button = tk.Button(root, text="Calculate Area", command=calculate_area)
area_button.pack()
circumference_button = tk.Button(root, text="Calculate Circumference", command=calculate_circumference)
circumference_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
