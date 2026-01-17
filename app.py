import tkinter as tk
from ui.login_ui import loginScreen
from ui.dashboard_ui import dashboardScreen
from ui.profile_ui import profileScreen
from ui.registration_ui import registrationScreen
from ui.tasks_ui import taskDashboard
from ui.add_task_ui import addTaskScreen
from ui.edit_task_ui import editTaskScreen
from ui.admin_dashboard import adminDashboard


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do App")
        self.geometry("500x500")
        self.configure(bg="#ffe6f0")
        self.current_user = None
        self.show_login()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear_screen()
        loginScreen(self).pack(fill="both", expand=True)

    def show_dashboard(self, user):
        self.current_user = user
        self.clear_screen()
        dashboardScreen(self, user).pack(fill="both", expand=True)

    def show_profile(self, user):
        self.clear_screen()
        profileScreen(self, user).pack(fill="both", expand=True)

    def show_registration(self):
        self.clear_screen()
        registrationScreen(self).pack(fill="both", expand=True)

    def show_tasks(self):
        self.clear_screen()
        taskDashboard(self, self.current_user).pack(fill="both", expand=True)
    
    def show_add_task(self):
        self.clear_screen()
        addTaskScreen(self, self.current_user).pack(fill="both", expand=True)

    def show_edit_task(self, task):
        self.clear_screen()
        editTaskScreen(self, self.current_user, task).pack(fill="both", expand=True)

    def show_admin_dashboard(self, user):
        self.current_user = user
        self.clear_screen()
        adminDashboard(self, user).pack(fill="both", expand=True)

