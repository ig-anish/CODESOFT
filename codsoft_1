import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json


class ToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("TO-DO Lisy Application")
        self.geometry("1000x600")
        style =Style(theme="flatly")
        style.configure("Custom.TEntry",foreground="lightgray")
        # Adding tasks
        self.tsk_in=ttk.Entry(self, font=("Arial",20), width=30, style="Custom.TEntry",)
        self.tsk_in.pack(pady=10)
        # Placeholder for input
        self.tsk_in.insert(0,"Enter your ToDo here...")
        self.tsk_in.bind("<FocusIn>",self.clear_placeholder)
        self.tsk_in.bind("<FocusOut>",self.restore_placeholder)
        # Button for adding task
        ttk.Button(self,text="Add", command=self.add_task).pack(pady=5)
        # Listbox to display added tasks
        self.tsk_li = tk.Listbox(self, font=("Arial", 20), height=10, selectmode=tk.BROWSE)
        self.tsk_li.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        # Buttons for marking tasks as done, updating, or deleting them
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, pady=10)
        ttk.Button(button_frame, text="Done",style="success.TButton", command=self.mark_done).pack(side=tk.LEFT, padx=20)
        ttk.Button(button_frame, text="Update", style="primary.TButton",command=self.update_task).pack(side=tk.LEFT, padx=20)
        ttk.Button(button_frame,text="Delete", style="danger.TButton",command=self.delete_task).pack(side=tk.LEFT, padx=20)
        # Button for displaying statistics
        ttk.Button(self, text="View Stats", style="info.TButton", command=self.view_stats).pack(side=tk.BOTTOM, pady=10)

        self.load_tasks()

    def view_stats(self):
        done_count=0
        total_count=self.tsk_li.size()
        for i in range(total_count):
            if self.tsk_li.itemcget(i,"fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics",f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    def add_task(self):
        task=self.tsk_in.get()
        if task and task != "Enter your ToDo here...":
            self.tsk_li.insert(tk.END, task)
            self.tsk_li.itemconfig(tk.END, fg="red")
            self.tsk_in.delete(0, tk.END)
            self.save_tasks()

    def mark_done(self):
        task_index=self.tsk_li.curselection()
        if task_index:
            self.tsk_li.itemconfig(task_index, fg="green")
            self.save_tasks()

    def delete_task(self):
        task_index=self.tsk_li.curselection()
        if task_index:
            self.tsk_li.delete(task_index)
            self.save_tasks()
    def update_task(self):
        task_index=self.tsk_li.curselection()
        if task_index:
            new_task = self.tsk_in.get()
            if new_task and new_task != "Enter your ToDo here...":
                self.tsk_li.delete(task_index)
                self.tsk_li.insert(task_index, new_task)
                self.tsk_li.itemconfig(task_index, fg="red")
                self.tsk_in.delete(0, tk.END)
                self.save_tasks()
    def clear_placeholder(self, event):
        if self.tsk_in.get() == "Enter your ToDo here...":
            self.tsk_in.delete(0, tk.END)
            self.tsk_in.configure(style="TEntry")
    def restore_placeholder(self, event):
        if self.tsk_in.get() == "":
            self.tsk_in.insert(0, "Enter your ToDo here...")
            self.tsk_in.configure(style="Custom.TEntry")
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
            for task in data:
                self.tsk_li.insert(tk.END, task["task"])
                self.tsk_li.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass
    def save_tasks(self):
        data = []
        for i in range(self.tsk_li.size()):
            text = self.tsk_li.get(i)
            color =self.tsk_li.itemcget(i, "fg")
            data.append({"task": text, "color": color})
        with open("tasks.json","w") as f:
            json.dump(data,f)




if __name__ == '__main__':
    app = ToDoListApp()
    app.mainloop()















