from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random

#change bg color
def change_color():
    color = random_color()
    root.config(bg=color)
    label.config(text=f"Background Color: {color}")

# function to generate hexadecimal code
def random_color():
    r = lambda: random.randint(0, 255)
    return('#%02X%02X%02X' % (r(), r(), r()))

#creating main window
root = ThemedTk(theme="yaru")
root.config(bg="white")
root.geometry("700x500")
root.title("Color-Flipper")

color_var = StringVar()

#buttons
btn = ttk.Button(root, text="Change Color", command=change_color)

# creating and configure label
label = Label(root, text="Background Color: ", bg="white", foreground="black")
label.pack()

#place width in the middle of the application
label.place(relx=0.5, rely=0.5, anchor="center")
btn.place(relx=0.5, rely=0.4, anchor="center")

root.mainloop()
