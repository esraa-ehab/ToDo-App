import tkinter as tk
from tkinter import messagebox
from services.task_manager import taskManager


THEME_BG = "#fdf2f6"
THEME_ACCENT = "#ff7aa2"
THEME_TEXT = "#2d2a32"

class taskDashboard(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master, bg=THEME_BG)
        self.user = user
        self.task_man = taskManager()
        self.build_ui()

    def build_ui(self):
        nav_bar = tk.Frame(self, bg=THEME_BG)
        nav_bar.pack(fill="x", pady=(0, 15))

        tk.Button(
            nav_bar,
            text="Back to dashboard",
            command=self.go_back,
            bg=THEME_BG,
            fg=THEME_TEXT,
            relief="flat",
            font=("Arial", 10, "bold")
        ).pack(side="left")

        tk.Button(
            nav_bar,
            text="Logout",
            command=self.logout,
            bg=THEME_BG,
            fg=THEME_ACCENT,
            relief="flat",
            font=("Arial", 10, "bold")
        ).pack(side="right")

        tk.Label(self, 
                text= f"Welcome {self.user.fname}",
                font= ("Arial", 24, "bold"),
                bg= THEME_BG,
                fg=THEME_TEXT
            ).pack(pady=(0,24))


        tk.Button(self,
                text="Add new task",
                font="Arial",
                command=self.master.show_add_task,
                bg=THEME_ACCENT,
                fg="black",
                activebackground="#ff5c90",
                relief="flat",
                padx=12,
                pady=8,
            ).pack(pady=18, fill="x")
        
        tasks_section = tk.Frame(self, bg="#ffffff", padx=20, pady=15)
        tasks_section.pack(fill="both", expand=True, pady=10, padx=10)
        tasks_section.pack_propagate(False)
        tasks_section.configure(height=300, width=450)

        tk.Label(
            tasks_section,
            text="Your Tasks",
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            fg=THEME_TEXT
        ).pack(anchor="w", pady=(0, 10))

        self.tasks_frame = tk.Frame(tasks_section, bg="#ffffff")
        self.tasks_frame.pack(fill="both", expand=True)

        self.load_tasks()

    def load_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        tasks = self.task_man.get_user_tasks(self.user.id)

        if not tasks:
            tk.Label(
                self.tasks_frame,
                text="No tasks yet",
                font=("Arial", 11),
                bg="#ffffff",
                fg=THEME_TEXT
            ).pack(pady=10)
            return
        
        for task_index, task in tasks:
            task_row = tk.Frame(self.tasks_frame, bg="#ffffff")
            task_row.pack(anchor="w", fill="x", pady=5)
            
            tk.Label(
                task_row,
                text=f"• {task['title']} [{task['status']}]",
                bg="#ffffff",
                fg=THEME_TEXT,
                font=("Arial", 10)
            ).pack(side="left", anchor="w")
            
            tk.Button(
                task_row,
                text="Delete",
                command=lambda idx=task_index: self.delete_task(idx),
                bg="#ffcccc",
                fg=THEME_TEXT,
                activebackground="#ffaaaa",
                relief="flat",
                bd=0,
                highlightthickness=0,
                highlightbackground="#ffcccc",
                padx=6,
                pady=2,
                font=("Arial", 8)
            ).pack(side="right", padx=2)
            
            tk.Button(
                task_row,
                text="Edit",
                command=lambda t=task: self.master.show_edit_task(t),
                bg="#e0e0e0",
                fg=THEME_TEXT,
                activebackground="#d0d0d0",
                relief="flat",
                bd=0,
                highlightthickness=0,
                highlightbackground="#e0e0e0",
                padx=6,
                pady=2,
                font=("Arial", 8)
            ).pack(side="right", padx=2)

    def delete_task(self, task_index):
        response = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this task?"
        )
        if response:
            self.task_man.delete_task(task_index)
            self.load_tasks()

    def logout(self):
        self.master.current_user = None
        self.master.show_login()

    def go_back(self):
        self.master.show_dashboard(self.user)
