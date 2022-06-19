from flask_bcrypt import Bcrypt

from Recipes import app
from Recipes.config.connection import SQL


class User:
    bcryptObject = Bcrypt(app)

    def __init__(self, data):
        self.id = data['idusers']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def getById(cls, data):
        query = "SELECT * FROM users WHERE idusers=%(idusers)s;"
        result = SQL("Flask_Registration").query(query, data)[0]
        return cls(result)

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        data['password'] = cls.bcryptObject.generate_password_hash(data['password'])
        SQL("Flask_Registration").query(query, data)

    @classmethod
    def validateLogin(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = SQL("Flask_Registration").query(query, data)
        print(result)
        if result:
            result = cls(result[0])
        else:
            return False

        if cls.bcryptObject.check_password_hash(result.password, data['password']):
            return result
        else:
            return False
