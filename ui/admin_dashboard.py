import tkinter as tk
from tkinter import messagebox

THEME_BG = "#fdf2f6"
THEME_ACCENT = "#ff7aa2"
THEME_TEXT = "#2d2a32"

class adminDashboard(tk.Frame):
    def __init__(self, master, admin):
        super().__init__(master, bg=THEME_BG)
        self.admin = admin
        self.configure(padx=24, pady=24)
        self.build_ui()

    def build_ui(self):
        # Header with logout button
        header = tk.Frame(self, bg=THEME_BG)
        header.pack(fill="x", pady=(0, 24))

        tk.Label(
            header,
            text="Admin Dashboard",
            font=("Arial", 24, "bold"),
            bg=THEME_BG,
            fg=THEME_TEXT
        ).pack(side="left")

        tk.Button(
            header,
            text="Logout",
            command=self.logout,
            bg=THEME_BG,
            fg=THEME_ACCENT,
            relief="flat",
            bd=0,
            highlightthickness=0,
            font=("Arial", 10, "bold")
        ).pack(side="right")

        # USERS SECTION
        self.build_users_section()

        # TASKS SECTION
        self.build_tasks_section()

    # ---------------- USERS ---------------- #
    def build_users_section(self):
        tk.Label(
            self,
            text="Users",
            font=("Arial", 16, "bold"),
            bg=THEME_BG,
            fg=THEME_TEXT
        ).pack(anchor="w")

        self.users_frame = tk.Frame(self, bg=THEME_BG)
        self.users_frame.pack(fill="x", pady=8)

        self.load_users()

    def load_users(self):
        for w in self.users_frame.winfo_children():
            w.destroy()

        users = self.admin.view_all_users()

        for user in users:
            row = tk.Frame(self.users_frame, bg="white", padx=10, pady=6)
            row.pack(fill="x", pady=4)

            tk.Label(
                row,
                text=f"{user['email']} ({user['status']})",
                bg="white",
                fg=THEME_TEXT
            ).pack(side="left")

            if user["status"] == "active":
                tk.Button(
                    row,
                    text="Deactivate",
                    command=lambda u=user: self.deactivate_user(u),
                    bg="#ffe1ea",
                    relief="flat",
                    bd=0,
                    highlightthickness=0,
                ).pack(side="right")

    def deactivate_user(self, user):
        confirm = messagebox.askyesno(
            "Confirm",
            f"Deactivate {user['email']}?"
        )
        if confirm:
            self.admin.deactivate_user(user["id"])
            self.load_users()

    # ---------------- TASKS ---------------- #
    def build_tasks_section(self):
        tk.Label(
            self,
            text="Tasks",
            font=("Arial", 16, "bold"),
            bg=THEME_BG,
            fg=THEME_TEXT
        ).pack(anchor="w", pady=(20, 0))

        self.tasks_frame = tk.Frame(self, bg=THEME_BG)
        self.tasks_frame.pack(fill="x", pady=8)

        self.load_tasks()

    def load_tasks(self):
        for w in self.tasks_frame.winfo_children():
            w.destroy()

        tasks = self.admin.view_all_tasks()

        for task in tasks:
            row = tk.Frame(self.tasks_frame, bg="white", padx=10, pady=6)
            row.pack(fill="x", pady=4)

            tk.Label(
                row,
                text=f"{task['title']} --> {task['owner_name']}",
                bg="white",
                fg=THEME_TEXT
            ).pack(side="left")

            tk.Button(
                row,
                text="Delete",
                command=lambda t=task: self.delete_task(t),
                bg="#ffd6d6",
                relief="flat",
                bd=0,
                highlightthickness=0,
            ).pack(side="right")

    def delete_task(self, task):
        confirm = messagebox.askyesno(
            "Confirm",
            f"Delete task '{task['title']}'?"
        )
        if confirm:
            self.admin.delete_task(task["task_id"])
            self.load_tasks()

    def logout(self):
        self.master.current_user = None
        self.master.show_login()
