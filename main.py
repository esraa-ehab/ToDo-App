from utils import save_users, load_users
from auth import authManager

auth_man = authManager()
current_user = None

while True:
    if not current_user:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Choose 1, 2, or 3: ")
        if choice == "1":
            auth_man.register()
        if choice == "2":
            current_user = auth_man.login()
        if choice == "3":
            break

    else:
        print(f"\nWelcome {current_user.fname}")
        print("\n1. Update your profile\n2. Logout")
        choice = input("Choose 1 or 2: ")
        if choice == "1":
            current_user.update_field(
                fname = input("Enter your new first name: "),
                lname = input("Enter your new last name: "),
                mobile = input("Enter your new mobile number: ")
            )

            users = load_users()
            for u in users:
                if u["email"] == current_user.email:
                    u.update(current_user.user_to_dict())
            save_users(users)
            print("Profile updated successfully")
        elif choice == "2":
            current_user = None
