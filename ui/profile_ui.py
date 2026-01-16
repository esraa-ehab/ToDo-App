import tkinter as tk
from tkinter import messagebox
from utils.helpers import load_users, save_users, valid_egyptian_phone


THEME_BG = "#fdf2f6"
THEME_ACCENT = "#ff7aa2"
THEME_TEXT = "#2d2a32"

class profileScreen(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master, bg=THEME_BG)
        self.configure(padx=24, pady=24)
        self.user = user
        self.build_ui()

    def build_ui(self):
        tk.Label(
            self,
            text="Update Profile",
            font=("Arial", 24, "bold"),
            bg=THEME_BG,
            fg=THEME_TEXT,
        ).pack(pady=(0, 16), anchor="w")

        tk.Label(self, text="New First Name", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.fname_entry = tk.Entry(self, bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 10))
        self.fname_entry.insert(0, self.user.fname)
        self.fname_entry.pack(anchor="w", pady=6, fill="x", ipady=6)

        tk.Label(self, text="New Last Name", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.lname_entry = tk.Entry(self, bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 10))
        self.lname_entry.insert(0, self.user.lname)
        self.lname_entry.pack(anchor="w", pady=6, fill="x", ipady=6)

        tk.Label(self, text="New Phone Number", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 10)).pack(anchor="w")
        self.mobile_entry = tk.Entry(self, bg="white", fg=THEME_TEXT, insertbackground="black", relief="flat", bd=0, highlightthickness=0, font=("Arial", 10))
        self.mobile_entry.insert(0, self.user.mobile)
        self.mobile_entry.pack(anchor="w", pady=6, fill="x", ipady=6)

        tk.Button(
            self,
            text="Save Changes",
            command=self.saveChanges,
            bg=THEME_ACCENT,
            fg="black",
            activebackground="#ff5c90",
            activeforeground="black",
            relief="flat",
            bd=0,
            padx=12,
            pady=10,
            font=("Arial", 11, "bold"),
        ).pack(pady=12, fill="x")

        tk.Button(
            self,
            text="Back to Dashboard",
            command=self.go_back,
            bg="#f0d0dc",
            fg="black",
            activebackground="#e3b8c8",
            activeforeground=THEME_TEXT,
            relief="flat",
            bd=0,
            padx=12,
            pady=8,
            font=("Arial", 11),
        ).pack(fill="x")

    def saveChanges(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        mobile = self.mobile_entry.get()

        if not valid_egyptian_phone(mobile):
            messagebox.showerror("Error", "Invalid Egyptian mobile number")
            return

        self.user.update_field(fname, lname, mobile)

        users = load_users()
        for u in users:
            if u["email"] == self.user.email:
                u.update(self.user.user_to_dict())

        save_users(users)
        messagebox.showinfo("Success", "Profile updated successfully")

    def go_back(self):
        self.master.show_dashboard(self.user)