import regex as re
class User:
    def __init__(self, id, fname, lname, email, password_hash, mobile, status="inactive", role="user"):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password_hash = password_hash
        self.mobile = mobile
        self.status = status
        self.role = role

    @staticmethod
    def validate_password_format(password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@$])[A-Za-z\d_@$]{8,}$"
        return re.fullmatch(pattern, password) is not None

    def check_password(self, password, hash_func):
        return self.validate_password_format(password) and (self.password_hash == hash_func(password))

    def update_field(self, fname = None, lname = None, mobile = None):
        if fname:
            self.fname = fname
        if lname:
            self.lname = lname
        if mobile:
            self.mobile = mobile

    def user_to_dict(self):
        return {
            "id": self.id,
            "fname": self.fname,
            "lname": self.lname,
            "email": self.email,
            "password_hash": self.password_hash,
            "mobile": self.mobile,
            "status": self.status,
            "role": self.role
        }