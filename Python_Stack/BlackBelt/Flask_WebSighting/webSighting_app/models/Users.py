from flask import flash
from flask_bcrypt import Bcrypt

from webSighting_app import app
from webSighting_app.config.connection import SQL
from .CreateDate import createDate
from .UpdateDate import updateDate


class User:
    dataBase = "Sasquatch_Websighting"
    bcrypt = Bcrypt(app)

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = createDate(data['created_at'])
        self.updated_at = updateDate(data['updated_at'])

    @classmethod
    def all(cls):
        query = "SELECT * FROM users;"
        results = SQL(cls.dataBase).query(query)

        if not results:
            return []

        users = []
        for user in results:
            users.append(cls(user))

        return users

    @classmethod
    def add(cls, data):
        data["password"] = cls.bcrypt.generate_password_hash(data['password'])
        query = 'INSERT INTO users(first_name, last_name, email, password) VALUE (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        SQL(cls.dataBase).query(query, data)
        return True

    @classmethod
    def getUserByEmail(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = SQL(cls.dataBase).query(query, data)
        if result:
            return cls(result[0])
        flash("User not registerd", "not_register_error")
        return False

    @classmethod
    def getUserById(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        result = SQL(cls.dataBase).query(query, data)
        if result:
            return cls(result[0])

    @classmethod
    def validatePassword(cls, value1, value2):
        isMatch = cls.bcrypt.check_password_hash(value1, value2)
        if isMatch:
            return True
        flash("Incorrect Password", "password_mismatch_error")

    @classmethod
    def removeUserById(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        SQL(cls.dataBase).query(query, data)

    @classmethod
    def updateUserById(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        SQL(cls.dataBase).query(query, data)

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
