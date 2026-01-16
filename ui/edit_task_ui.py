import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from services.task_manager import taskManager

THEME_BG = "#fdf2f6"
THEME_ACCENT = "#ff7aa2"
THEME_TEXT = "#2d2a32"

class editTaskScreen(tk.Frame):
    def __init__(self, master, user, task):
        super().__init__(master, bg=THEME_BG)
        self.user = user
        self.task = task
        self.task_man = taskManager()
        self.configure(padx=24, pady=24)
        self.build_ui()

    def build_ui(self):
        tk.Label(
            self,
            text="Edit Task",
            font=("Arial", 24, "bold"),
            bg=THEME_BG,
            fg=THEME_TEXT
        ).pack(pady=(0, 24), anchor="w")

        form = tk.Frame(self, bg="#fdf2f6", padx=20, pady=20, bd=0, highlightthickness=0)
        form.pack(fill="x", padx=10)

        tk.Label(form, text="Title", bg="#fdf2f6", fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.title_entry = tk.Entry(form, bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 10))
        self.title_entry.pack(fill="x", pady=6, ipady=6)
        self.title_entry.insert(0, self.task["title"])

        tk.Label(form, text="Description", bg="#fdf2f6", fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.desc_entry = tk.Entry(form, bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 10))
        self.desc_entry.pack(fill="x", pady=6, ipady=6)
        self.desc_entry.insert(0, self.task["description"])

        tk.Label(form, text="Priority", bg="#fdf2f6", fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.priority_var = tk.StringVar(value=self.task["priority"])
        priority_menu = tk.OptionMenu(
            form,
            self.priority_var,
            "Low", "Medium", "High"
        )
        priority_menu.config(bg="white", relief="flat", highlightthickness=0, bd=0, font=("Arial", 10), fg=THEME_TEXT)
        priority_menu["menu"].config(bg="white", fg=THEME_TEXT)
        priority_menu.pack(fill="x", pady=6, ipady=4)

        tk.Label(form, text="Due Date (DD-MM-YY)", bg="#fdf2f6", fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.date_entry = tk.Entry(form, bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 10))
        self.date_entry.pack(fill="x", pady=6, ipady=6)
        self.date_entry.insert(0, self.task["due_date"])

        tk.Label(form, text="Status", bg="#fdf2f6", fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.status_var = tk.StringVar(value=self.task["status"])
        status_menu = tk.OptionMenu(
            form,
            self.status_var,
            "Pending", "Completed"
        )
        status_menu.config(bg="white", relief="flat", highlightthickness=0, bd=0, font=("Arial", 10), fg=THEME_TEXT)
        status_menu["menu"].config(bg="white", fg=THEME_TEXT)
        status_menu.pack(fill="x", pady=6, ipady=4)

        tk.Button(
            form,
            text="Save Changes",
            bg=THEME_ACCENT,
            fg="black",
            activebackground="#ff5c90",
            relief="flat",
            bd=0,
            padx=12,
            pady=10,
            font=("Arial", 11, "bold"),
            command=self.save_changes
        ).pack(pady=(18, 6), fill="x")

        tk.Button(
            form,
            text="Cancel",
            bg="#f0d0dc",
            fg="black",
            relief="flat",
            bd=0,
            padx=12,
            pady=8,
            font=("Arial", 11),
            command=self.master.show_tasks
        ).pack(fill="x")

    def save_changes(self):
        try:
            datetime.strptime(self.date_entry.get(), "%d-%m-%y")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format (DD-MM-YY)")
            return

        updated_data = {
            "title": self.title_entry.get(),
            "description": self.desc_entry.get(),
            "priority": self.priority_var.get(),
            "due_date": self.date_entry.get(),
            "status": self.status_var.get()
        }

        tasks = self.task_man.get_user_tasks(self.user.id)
        task_index = None
        for idx, (i, t) in enumerate(tasks):
            if t["title"] == self.task["title"] and t["created_at"] == self.task["created_at"]:
                task_index = i
                break

        if task_index is not None:
            self.task_man.edit_task(task_index, updated_data)
            messagebox.showinfo("Success", "Task updated successfully")
            self.master.show_tasks()
        else:
            messagebox.showerror("Error", "Could not find task to update")
