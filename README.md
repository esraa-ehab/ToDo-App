# ToDo App

A simple task management application built with Python and Tkinter for managing daily tasks and user accounts.

## Features

- User registration and login with password hashing
- Create, edit, and delete tasks
- Search tasks by keyword
- Filter tasks by priority and status
- Sort tasks by due date, priority, or status
- User profile management
- Admin dashboard for managing all users and tasks
- Responsive design that adjusts to window size

## Requirements

- Python 3.7 or higher
- Tkinter (usually included with Python)
- regex module
- hashlib (included with Python)

## Installation

1. Clone or download the project
2. Make sure you have Python installed
3. Install required packages:
   pip install regex

4. Run the application:
   python main.py

## File Structure

- app.py: Main application controller
- main.py: Entry point
- models/: Data models (User, Task, Admin)
- services/: Business logic (authentication, task management)
- ui/: User interface screens
- utils/: Helper functions
- data/: Data storage (JSON files)

## How to Use

### Logging In

Start the app and enter your email and password. If you're new, click Register to create an account.

### User Dashboard

After logging in, you'll see the main dashboard with options to view your tasks or update your profile.

### Task Management

Click on Tasks Dashboard to manage your tasks. You can:
- Add new tasks
- Search for tasks
- Filter by priority or status
- Sort by different criteria
- Edit or delete existing tasks

### Admin Dashboard

If you have admin privileges, you'll be directed to the admin dashboard instead. Here you can:
- View all users and their status
- Deactivate user accounts
- View and delete any task

## Data Storage

The app uses JSON files for storage:
- users.json: Stores user accounts and profiles
- tasks.json: Stores all tasks

## Notes

- Passwords are hashed using SHA256 for security
- Tasks require a title and valid date format (DD-MM-YY)
- Inactive accounts cannot log in
- Admin accounts have access to system management features
