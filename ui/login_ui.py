import tkinter as tk
from tkinter import messagebox
from services.auth import authManager


THEME_BG = "#fdf2f6"
THEME_ACCENT = "#ff7aa2"
THEME_TEXT = "#2d2a32"

class loginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=THEME_BG)
        self.configure(padx=60, pady=60)
        self.auth = authManager()
        self.build_ui()

    def build_ui(self):
        tk.Label(
            self,
            text="Login",
            font=("Arial", 32, "bold"),
            bg=THEME_BG,
            fg=THEME_TEXT,
        ).pack(pady=(0, 36))

        tk.Label(self, text="Email", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 12)).pack(anchor="w")
        self.email_entry = tk.Entry(self, width=32, bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 12))
        self.email_entry.pack(anchor="w", pady=8, fill="x", ipady=8)

        tk.Label(self, text="Password", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 12)).pack(anchor="w")
        self.password_entry = tk.Entry(self, width=32, show="*", bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 12))
        self.password_entry.pack(anchor="w", pady=8, fill="x", ipady=8)

        tk.Button(
            self,
            text="Login",
            command=self.login,
            bg=THEME_ACCENT,
            fg="black",
            activebackground="#ff5c90",
            relief="flat",
            bd=0,
            padx=16,
            pady=12,
            font=("Arial", 13, "bold"),
        ).pack(pady=24, fill="x")

        tk.Button(
            self, 
            text="Register", 
            command=self.master.show_registration, 
            bg=THEME_ACCENT, 
            fg="black",
            activebackground="#ff5c90",
            relief="flat",
            bd=0,
            padx=16,
            pady=10,
            font=("Arial", 13),
        ).pack(pady=8)


    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        user = self.auth.login(email, password)

        if user:
            if user.role == "admin":
                self.master.show_admin_dashboard(user)
            else:
                self.master.show_dashboard(user)
        else:
            messagebox.showerror("Error", "Invalid credentials or inactive account")
