from models.user import User
from models.admin import Admin
from utils.helpers import *

class authManager():
    def __init__(self):
        pass
    def register(self):
        users = load_users()

        id = input("Enter your ID (14 Digits): ")
        if not valid_id(id):
            print("Invalid ID")
            return 
        
        if any(u['id'] == id for u in users):
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
            password_hash=hash_password(password),
            mobile=phone_num,
            status="active",
            role="user"
        )
        users.append(user.user_to_dict())
        save_users(users)
        print("Regestration Successful")

    def login(self, email, password):
        users = load_users()

        for u in users:
            if u["email"] == email:
                if u["status"] != "active":
                    print("This user is not active")
                    return 
                
                if u["password_hash"] == hash_password(password):
                    if u["role"] == "admin":
                        print("login successful")
                        return Admin(**u)
                    else:
                        print("login successful")
                        return User(**u)
        print("user not found")
        return  