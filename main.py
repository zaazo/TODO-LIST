import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Material Todo List App")
        self.root.configure(bg='#212121')  # Dark grey background
        self.root.geometry("400x500")

        self.tasks = []

        self.task_label = tk.Label(root, text="Task:", fg='white', bg='#212121', font=('Roboto', 16, 'bold'))
        self.task_label.pack()

        self.task_entry = tk.Entry(root, width=30, font=('Roboto', 12))
        self.task_entry.pack()

        self.importance_label = tk.Label(root, text="Importance:", fg='white', bg='#212121', font=('Roboto', 16, 'bold'))
        self.importance_label.pack()

        self.importance_var = tk.StringVar(root)
        self.importance_var.set("low")  # Default importance
        self.importance_dropdown = tk.OptionMenu(root, self.importance_var, "low", "mid", "high")
        self.importance_dropdown.config(bg='#212121', fg='white', font=('Roboto', 12), highlightthickness=0)
        self.importance_dropdown.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg='#4CAF50', fg='white', font=('Roboto', 14, 'bold'), relief=tk.GROOVE)
        self.add_button.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=35, height=10, bg='#424242', fg='white', font=('Roboto', 12))
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg='#FF5722', fg='white', font=('Roboto', 14, 'bold'), relief=tk.GROOVE)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        importance = self.importance_var.get()
        if task:
            self.tasks.append((task, importance))
            self.task_listbox.insert(tk.END, f"{task} - {importance}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
