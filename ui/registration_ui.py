import tkinter as tk
from tkinter import messagebox
from utils.helpers import valid_egyptian_phone, valid_email, hash_password, load_users, save_users
from services.auth import authManager
from models.user import User

THEME_BG = "#fdf2f6"
THEME_ACCENT = "#ff7aa2"
THEME_TEXT = "#2d2a32"

class registrationScreen(tk.Frame):
    def __init__(self, master, user=None):
        super().__init__(master, bg = THEME_BG)
        self.configure(padx=24, pady=24)
        self.user = user
        self.auth = authManager()
        self.build_ui()

    def build_ui(self):
        tk.Label(
            self,
            text="Register",
            font=("Arial", 24, "bold"),
            bg=THEME_BG,
            fg=THEME_TEXT,
        ).pack(pady=(0, 24))

        tk.Label(self, text="ID Number", bg=THEME_BG, fg=THEME_TEXT).pack(anchor="w")
        self.id_entry = tk.Entry(self, width=32, bg="white", fg=THEME_TEXT, relief="flat")
        self.id_entry.pack()

        tk.Label(self, text="First Name", bg=THEME_BG, fg=THEME_TEXT).pack(anchor="w")
        self.fname_entry = tk.Entry(self, width=32, bg="white", fg=THEME_TEXT, relief="flat")
        self.fname_entry.pack(anchor="w", pady=6, fill="x")

        tk.Label(self, text="Last Name",bg=THEME_BG, fg=THEME_TEXT).pack(anchor="w")
        self.lname_entry = tk.Entry(self, width=32, bg="white", fg=THEME_TEXT, relief="flat")
        self.lname_entry.pack(anchor="w", pady=6, fill="x")

        tk.Label(self, text="Email",bg=THEME_BG, fg=THEME_TEXT).pack(anchor="w")
        self.email_entry = tk.Entry(self, width=32, bg="white", fg=THEME_TEXT, relief="flat")
        self.email_entry.pack(anchor="w", pady=6, fill="x")

        tk.Label(self, text="Password", bg=THEME_BG, fg=THEME_TEXT).pack(anchor="w")
        self.password_entry = tk.Entry(self, show="*", width=32, bg="white", fg=THEME_TEXT, relief="flat")
        self.password_entry.pack(anchor="w", pady=6, fill="x")

        tk.Label(self, text="Confirm Password", bg=THEME_BG, fg=THEME_TEXT).pack(anchor="w")
        self.confirm_entry = tk.Entry(self, show="*", width=32, bg="white", fg=THEME_TEXT, relief="flat")
        self.confirm_entry.pack(anchor="w", pady=6, fill="x")

        tk.Label(self, text="Mobile Number", bg=THEME_BG, fg=THEME_TEXT).pack(anchor="w")
        self.mobile_entry = tk.Entry(self, width=32, bg="white", fg=THEME_TEXT, relief="flat")
        self.mobile_entry.pack(anchor="w", pady=6, fill="x")

        tk.Button(self,
                text="Register", 
                command=self.register, 
                bg=THEME_ACCENT, 
                fg="black",
                activebackground="#ff5c90",
                relief="flat",
                padx=12,
                pady=8,
            ).pack(pady=18, fill="x")
        tk.Button(self, 
                text="Back to Login",
                command=self.master.show_login, 
                bg=THEME_ACCENT, 
                fg="black",
                activebackground="#ff5c90",
                relief="flat",
                padx=12,
                pady=8,
            ).pack(pady=18, fill="x")
    
    def register(self):
        id = self.id_entry.get().strip()
        fname = self.fname_entry.get().strip()
        lname = self.lname_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()
        mobile = self.mobile_entry.get().strip()

        # Validations
        if not all([id, fname, lname, email, password, confirm, mobile]):
            messagebox.showerror("Error", "All fields are required")
            return

        if len(id) != 14 or not id.isdigit():
            messagebox.showerror("Error", "ID must be 14 digits")
            return
        if not valid_email(email):
            messagebox.showerror("Error", "Invalid email")
            return
        if not User.validate_password_format(password):
            messagebox.showerror("Error", "Invalid password: must be 8+ chars with uppercase, lowercase, digit, and special char (_@$)")
            return
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return
        if not valid_egyptian_phone(mobile):
            messagebox.showerror("Error", "Invalid Egyptian mobile number")
            return
        
        users = load_users()
        if any(u['id'] == id for u in users):
            messagebox.showerror("Error", "ID already registered")
            return
        
        if any(u['email'] == email for u in users):
            messagebox.showerror("Error", "Email already registered")
            return
        
        user = User(
            id=id,
            fname=fname,
            lname=lname,
            email=email,
            password_hash=hash_password(password),
            mobile=mobile,
            status="active",
            role="user"
        )
        
        users.append(user.user_to_dict())
        save_users(users)
        
        messagebox.showinfo("Success", "Registration successful!")
        self.master.show_login()
