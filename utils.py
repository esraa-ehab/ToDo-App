import regex as re
import json
import hashlib
from datetime import datetime

user_file = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def valid_egyptian_phone(phone):
    return re.match(r"^(010|011|012|015)\d{8}$", phone)

def valid_id(id_number):
    return id_number.isdigit() and len(id_number) == 14

def save_user(users):
    with open(user_file, "w") as f:
        json.dump(users, f, indent=4)

def load_user(users):
    try:
        with open(user_file, "r") as f:
            json.load(f)
    except FileNotFoundError:
        return {}
