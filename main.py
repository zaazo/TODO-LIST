import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Minimal TodoList App")
        self.master.geometry("400x300")
        self.master.configure(bg='#222')
        
        self.tasks = []
        
        self.input_frame = tk.Frame(self.master, bg='#222')
        self.input_frame.pack(pady=10)
        
        self.task_label = tk.Label(self.input_frame, text="Task:", bg='#222', fg='white')
        self.task_label.grid(row=0, column=0, padx=5)
        
        self.task_entry = tk.Entry(self.input_frame, width=30)
        self.task_entry.grid(row=0, column=1, padx=5)
        
        self.importance_label = tk.Label(self.input_frame, text="Importance:", bg='#222', fg='white')
        self.importance_label.grid(row=0, column=2, padx=5)
        
        self.importance_var = tk.StringVar(self.master)
        self.importance_var.set("Low")  # default importance
        
        self.importance_option_menu = tk.OptionMenu(self.input_frame, self.importance_var, "Low", "Mid", "High")
        self.importance_option_menu.config(bg='#222', fg='white', highlightbackground='#222')
        self.importance_option_menu.grid(row=0, column=3, padx=5)
        
        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task, bg='#64b5f6', fg='white', relief=tk.FLAT)
        self.add_button.grid(row=0, column=4, padx=5)
        
        self.task_frame = tk.Frame(self.master, bg='#222')
        self.task_frame.pack(pady=10)
        
    def add_task(self):
        task_text = self.task_entry.get()
        importance = self.importance_var.get()
        
        if task_text.strip() != "":
            self.tasks.append((task_text, importance))
            self.display_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    
    def display_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        
        for i, task in enumerate(self.tasks, start=1):
            task_text, importance = task
            task_label = tk.Label(self.task_frame, text=f"{i}. {task_text} - {importance}", bg='#222', fg='white')
            task_label.pack(anchor=tk.W, pady=5)
            
            delete_button = tk.Button(self.task_frame, text="Delete", bg='#f44336', fg='white', relief=tk.FLAT, command=lambda index=i-1: self.delete_task(index))
            delete_button.pack(anchor=tk.W, pady=5)
    
    def delete_task(self, index):
        del self.tasks[index]
        self.display_tasks()

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
