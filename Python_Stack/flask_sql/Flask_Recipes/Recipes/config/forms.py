import re

from .passwordValidator import Password


class RegistrationForm:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.c_password = data['c_password']

    def validate_FirstName(self):
        if len(self.first_name) < 3:
            return False
        return True

    def validate_LastName(self):
        if len(self.last_name) < 3:
            return False
        return True

    def validate_Email(self):
        passwordRegEx = re.compile(r"^\S+@\S+$")
        return True if passwordRegEx.match(self.email) else False

    def validate_Password(self):
        return Password().validate(self.password)

    def isValid(self):
        return {
            "first_name": [self.validate_FirstName(), "First Name must be atleast 3 character"],
            "last_name": [self.validate_LastName(), "Last Name must be atleast 3 character"],
            "email": [self.validate_Email(), "Not a Valid Email Address"],
            "password": [self.validate_Password(),
                         "Password must be atleast 8 character long with number and special characters"],
            "c_password": [self.validate_cPassword() and self.validate_Password(),
                           "Password is not matching with confirm password"]
        }

    def getData(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password
        }

    def validate_cPassword(self):
        return self.password == self.c_password