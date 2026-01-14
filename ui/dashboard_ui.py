import tkinter as tk


THEME_BG = "#fdf2f6"
THEME_ACCENT = "#ff7aa2"
THEME_TEXT = "#2d2a32"


class dashboardScreen(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master, bg=THEME_BG)
        self.configure(padx=24, pady=24)
        self.user = user
        self.build_ui()

    def build_ui(self):
        tk.Label(
            self,
            text=f"Welcome, {self.user.fname}",
            font=("Arial", 22, "bold"),
            bg=THEME_BG,
            fg=THEME_TEXT,
        ).pack(pady=(0, 20), anchor="w")

        tk.Button(
            self,
            text="Update Profile",
            width=22,
            command=self.go_to_profile,
            bg=THEME_ACCENT,
            fg="black",
            activebackground="#ff5c90",
            activeforeground="white",
            relief="flat",
            padx=12,
            pady=8,
        ).pack(pady=6, fill="x")

        tk.Button(
            self,
            text="Logout",
            width=22,
            command=self.logout,
            bg="#f0d0dc",
            fg="black",
            activebackground="#e3b8c8",
            activeforeground=THEME_TEXT,
            relief="flat",
            padx=12,
            pady=8,
        ).pack(pady=6, fill="x")

    def logout(self):
        self.master.current_user = None
        self.master.show_login()

    def go_to_profile(self):
        self.master.show_profile(self.user)
        