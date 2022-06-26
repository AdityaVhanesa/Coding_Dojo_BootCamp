import re


class Password:
    def __init__(self):
        self.minLength = 8
        self.maxLength = 255
        self.specialCharacterRegEx = re.compile(r"[#$%^&!@*]")

    def validateLength(self, value):
        if 8 <= len(value) <= 255:
            return True
        return False

    def validateSpecialChar(self, value):
        A = self.specialCharacterRegEx.findall(value)
        return True if self.specialCharacterRegEx.findall(value) else False

    def validate(self, value):
        return self.validateLength(value) and self.validateSpecialChar(value) and not value.isalpha()
