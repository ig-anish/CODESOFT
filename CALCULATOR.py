import customtkinter as ctk

# Function to handle button click
def button_click(value):
    current_text = entry.get()
    entry.delete(0, ctk.END)
    entry.insert(ctk.END, current_text + value)

# Function to clear the entry field
def clear():
    entry.delete(0, ctk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, ctk.END)
        entry.insert(ctk.END, str(result))
    except Exception as e:
        entry.delete(0, ctk.END)
        entry.insert(ctk.END, "Error")

# Create the main window
root = ctk.CTk()
root.title("CALCULATOR")
root.geometry("338x480")

# Entry field to display the expression/result
entry = ctk.CTkEntry(root, width=300, justify='right', font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+'
]

# Place buttons in a grid
row = 1
col = 0
for button in buttons:
    if button == '=':
        btn = ctk.CTkButton(root, text=button, command=evaluate, width=75, height=75)
    else:
        btn = ctk.CTkButton(root, text=button, command=lambda b=button: button_click(b), width=75, height=75)
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
clear_button = ctk.CTkButton(root, text="C", command=clear, width=75, height=75)
clear_button.grid(row=row, column=0, columnspan=4, padx=5, pady=5, sticky='we')

# Start the main loop
root.mainloop()
