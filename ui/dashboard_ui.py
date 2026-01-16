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

        content = tk.Frame(self, bg=THEME_BG)
        content.pack(expand=True)

        tk.Button(
            content,
            text="Tasks Dashboard",
            font=("Arial", 14, "bold"),
            command=self.master.show_tasks,
            bg=THEME_ACCENT,
            fg="black",
            activebackground="#ff5c90",
            relief="flat",
            padx=20,
            pady=14,
        ).pack(pady=(10, 30), fill="x")

        actions = tk.Frame(content, bg=THEME_BG)
        actions.pack(fill="x")

        tk.Button(
            actions,
            text="Update Profile",
            command=self.go_to_profile,
            bg="#f0d0dc",
            relief="flat",
            padx=12,
            pady=8,
        ).pack(side="left", expand=True, fill="x", padx=(0, 8))

        tk.Button(
            actions,
            text="Logout",
            command=self.logout,
            bg="#f0d0dc",
            relief="flat",
            padx=12,
            pady=8,
        ).pack(side="left", expand=True, fill="x")


    def logout(self):
        self.master.current_user = None
        self.master.show_login()

    def go_to_profile(self):
        self.master.show_profile(self.user)
        