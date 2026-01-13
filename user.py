import regex as re
class user:
    def __init__(self, id, fname, lname, email, password_hash, mobile_n, status="inactive", role="user"):
        self.id = id
        self.fname = fname,
        self.lname = lname,
        self.email = email,
        self.password_hash = password_hash,
        self.mobile_n = mobile_n,
        self.status = status,
        self.role = role,

    def check_password(self, password, hash_func):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@$])[A-Za-z\d_@$]{8,}$"
        return (re.fullmatch(pattern, self.password)) and (self.password_hash == hash_func(password))

    def update_field(self, fname = None, lname = None, mobile_n = None):
        if fname:
            self.fname = fname
        if lname:
            self.fname = fname
        if mobile_n:
            self.mobile_n

    def user_to_dict(self):
        return {
            "ID": self.id,
            "first_name": self.fname,
            "last_name": self.lname,
            "email": self.email,
            "password_hash": self.password_hash,
            "mobile": self.mobile_n,
            "status": self.status,
            "role": self.role
        }