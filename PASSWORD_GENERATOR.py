import random
import string
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from customtkinter import *
set_appearance_mode("dark")

#generate password
def generate_password():
    ch = string.ascii_letters +  string.digits + string.punctuation
    password = "".join(random.choice(ch) for i in range(var.get()))
    output.config(text = password)
    output.config(text=password, font=("Arial", 20), justify = 'center')

#copy password
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output['text'])
#creating window
root= ThemedTk(theme = "equilux")
root.title("PASSWORD-GENERATOR")
root.geometry("400x300")

#variable to hold the no. of character
var = tk.IntVar()
var.set(8)

#combobox  menu
combobox = ttk.Combobox(root, textvariable=var, values=[8,9,10,12,13,14,15,16,17,18,19,20])
combobox .pack(pady=5)

# creating generate button
gen_btn = CTkButton(root, text="Generate", command= generate_password, corner_radius=32, fg_color="#C850C0",
                hover_color="#4158D0",border_color="#FFCC70",border_width=2)
gen_btn.place(relx=0.5, rely=0.5, anchor="center")


# copy button
copy_btn = CTkButton(root, text="Copy", command= copy_to_clipboard, corner_radius=32, fg_color="#C850C0",
                hover_color="#4158D0",border_color="#FFCC70",border_width=2)
copy_btn.place(relx=0.5, rely=0.7, anchor="center")


#creating output
output = ttk.Label(root)
output.pack(pady=20)

root.mainloop()