from user import User
from utils import *

class authManager():
    def register():
        users = load_users()

        id = input("Enter your ID (14 Digits): ")
        if not valid_id(id):
            print("Invalid ID")
            return 
        
        if any(u['ID'] == id for u in users):
            print("ID already exists")
            return
        
        email = input("Enter your email: ")
        if not valid_email(email):
            print("Invalid Email")
            return
        
        if any(u['email'] == email for u in users):
            print("Email already exists")
            return
        
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        if password != confirm_password:
            print("Password does not match") 
            return
        
        phone_num = input("Enter your phone number: ")
        if not valid_egyptian_phone(phone_num):
            print("Invalid Egyptian phone number") 
            return
        
        user = User(
            id=id,
            fname=input("Enter your first name: "),
            lname=input("Enter your last name: "),
            email=email,
            password_hash=password,
            mobile=phone_num,
            status="active",
            role="user"
        )
        users.append(user.user_to_dict())
        save_users(users)
        print("Regestration Successful")

    def login():
        users = load_users()
        email = input("Email: ")
        password = input("Password: ")
        for u in users:
            if u["email"] == email:
                if u["status"] != "active":
                    print("This user is not active")
                    return
                
                if u["password_hash"] == hash_password(password):
                    print("login successful")
                    return User(**u)
            print("user not found")
            return 