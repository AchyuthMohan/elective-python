import tkinter as tk

def convert_rupees_to_euro():
    try:
        rupees = float(rupees_entry.get())
        euro = rupees / 88.48  
        euro_entry.delete(0, tk.END)
        euro_entry.insert(tk.END, euro)
    except ValueError:
        euro_entry.delete(0, tk.END)
        euro_entry.insert(tk.END, "Invalid input")

def convert_euro_to_rupees():
    try:
        euro = float(euro_entry.get())
        rupees = euro * 88.48  
        rupees_entry.delete(0, tk.END)
        rupees_entry.insert(tk.END, rupees)
    except ValueError:
        rupees_entry.delete(0, tk.END)
        rupees_entry.insert(tk.END, "Invalid input")

window = tk.Tk()
window.title("Currency Converter")

rupees_label = tk.Label(window, text="Indian Rupees:")
rupees_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

euro_label = tk.Label(window, text="Euros:")
euro_label.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E)

rupees_entry = tk.Entry(window)
rupees_entry.insert(tk.END, "0.0")
rupees_entry.grid(row=1, column=0, padx=10, pady=10)

euro_entry = tk.Entry(window)
euro_entry.insert(tk.END, "0.0")
euro_entry.grid(row=1, column=1, padx=10, pady=10)

rupees_to_euro_button = tk.Button(window, text="R->E", command=convert_rupees_to_euro)
rupees_to_euro_button.grid(row=2, column=0, padx=10, pady=10)

euro_to_rupees_button = tk.Button(window, text="E->R", command=convert_euro_to_rupees)
euro_to_rupees_button.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
