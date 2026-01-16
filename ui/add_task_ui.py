import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from models.task import Task
from services.task_manager import taskManager


THEME_BG = "#fdf2f6"
THEME_ACCENT = "#ff7aa2"
THEME_TEXT = "#2d2a32"

class addTaskScreen(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master, bg=THEME_BG)
        self.user = user
        self.task_man = taskManager()
        self.build_ui()

    def build_ui(self):
        container = tk.Frame(self, bg=THEME_BG)
        container.pack(expand=True)

        tk.Label(
            container,
            text="Add New Task",
            font=("Arial", 24, "bold"),
            bg=THEME_BG,
            fg=THEME_TEXT
        ).pack(pady=(0, 24))

        form = tk.Frame(container, bg="#fdf2f6", padx=20, pady=20, bd=0, highlightthickness=0)
        form.pack(fill="x", padx=10)

        tk.Label(form, text="Title", bg="#fdf2f6", fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.title_entry = tk.Entry(form, bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 10))
        self.title_entry.pack(fill="x", pady=(4, 12), ipady=6)

        tk.Label(form, text="Description", bg="#fdf2f6", fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.desc_entry = tk.Entry(form, bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 10))
        self.desc_entry.pack(fill="x", pady=(4, 12), ipady=6)

        tk.Label(form, text="Priority", bg="#fdf2f6", fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.priority_var = tk.StringVar(value="Low")

        self.priority_menu = tk.OptionMenu(
            form,
            self.priority_var,
            "Low", "Medium", "High"
        )
        self.priority_menu.config(
            bg="white",
            fg=THEME_TEXT,
            relief="flat",
            highlightthickness=0,
            bd=0,
            font=("Arial", 10)
        )
        self.priority_menu["menu"].config(bg="white", fg=THEME_TEXT)
        self.priority_menu.pack(fill="x", pady=(4, 12), ipady=4)

        tk.Label(form, text="Due Date (DD-MM-YY)", bg="#fdf2f6", fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.date_entry = tk.Entry(form, bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 10))
        self.date_entry.pack(fill="x", pady=(4, 16), ipady=6)

        tk.Button(
            form,
            text="Save Task",
            bg=THEME_ACCENT,
            fg="black",
            activebackground="#ff5c90",
            relief="flat",
            bd=0,
            pady=10,
            font=("Arial", 11, "bold"),
            command=self.save_task
        ).pack(fill="x", pady=(0, 10))

        tk.Button(
            form,
            text="Back to Tasks",
            bg="#f0d0dc",
            fg=THEME_TEXT,
            relief="flat",
            bd=0,
            pady=8,
            font=("Arial", 11),
            command=self.master.show_tasks
        ).pack(fill="x")


    def save_task(self):
        title = self.title_entry.get()
        due_date = self.date_entry.get()

        if not title:
            messagebox.showerror("Error", "Title is required")
            return

        try:
            datetime.strptime(due_date, "%d-%m-%y")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format")
            return

        task = Task(
            task_id=None,
            title=title,
            description=self.desc_entry.get(),
            priority=self.priority_var.get(),
            owner_id=self.user.id,
            owner_name=self.user.fname,
            due_date=due_date
        )

        self.task_man.add_task(task)
        messagebox.showinfo("Success", "Task added successfully")
        self.master.show_tasks()
        