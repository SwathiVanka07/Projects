import tkinter as tk
from tkinter import messagebox, filedialog

class TodoApp:
    def __init__(self, root): 
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")

        # Title label
        tk.Label(self.root, text="My To-Do List", font=("Helvetica", 16)).pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(self.root, font=("Helvetica", 12), width=30)
        self.task_entry.pack(pady=10)

        # Add Task Button
        tk.Button(self.root, text="Add Task", width=15, command=self.add_task).pack()

        # Listbox to display tasks
        self.listbox = tk.Listbox(self.root, font=("Helvetica", 12), width=40, height=10)
        self.listbox.pack(pady=20)

        # Buttons for actions
        tk.Button(self.root, text="Delete Selected", width=15, command=self.delete_task).pack(pady=5)
        tk.Button(self.root, text="Save Tasks", width=15, command=self.save_tasks).pack(pady=5)
        tk.Button(self.root, text="Load Tasks", width=15, command=self.load_tasks).pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected[0])
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def save_tasks(self):
        tasks = self.listbox.get(0, tk.END)
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt")])
        if filepath:
            with open(filepath, "w") as f:
                for task in tasks:
                    f.write(task + "\n")
            messagebox.showinfo("Success", "Tasks saved successfully.")

    def load_tasks(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filepath:
            self.listbox.delete(0, tk.END)
            with open(filepath, "r") as f:
                for line in f:
                    self.listbox.insert(tk.END, line.strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
