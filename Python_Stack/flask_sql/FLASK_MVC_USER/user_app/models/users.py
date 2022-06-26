from user_app.config.connection import SQL


class createDate:
    def __init__(self, dateTime):
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.dateTime = dateTime

    def __str__(self):
        return f"{self.days[self.dateTime.weekday()]} {self.dateTime.day}, {self.dateTime.year}"


class updateDate:
    def __init__(self, dateTime):
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.dateTime = dateTime

    def __str__(self):
        return f"{self.days[self.dateTime.weekday()]} {self.dateTime.day}, {self.dateTime.year} at {self.dateTime.time()}"


class USER:
    dataBase = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
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
        query = 'INSERT INTO users(first_name, last_name, email) VALUE (%(first_name)s, %(last_name)s, %(email)s);'
        return SQL(cls.dataBase).query(query, data)

    @classmethod
    def getUserById(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        result = SQL(cls.dataBase).query(query, data)
        if result:
            return cls(result[0])

    @classmethod
    def removeUserById(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        SQL(cls.dataBase).query(query, data)

    @classmethod
    def updateUserById(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        SQL(cls.dataBase).query(query, data)
