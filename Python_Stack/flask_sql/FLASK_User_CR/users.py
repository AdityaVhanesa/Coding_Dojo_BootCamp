from datetime import datetime

from connection import SQL


class date:
    def __init__(self, dateTime):
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.dateTime = dateTime

    def __str__(self):
        return f"{self.days[self.dateTime.weekday()]} {self.dateTime.day}, {self.dateTime.year}"


class USER:
    dataBase = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = date(data['created_at'])
        self.updated_at = date(data['updated_at'])

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
        query = 'INSERT INTO users(first_name, last_name, email) VALUE (%(first_name)s, %(last_name)s, %(email)s);'
        return SQL(cls.dataBase).query(query, data)
