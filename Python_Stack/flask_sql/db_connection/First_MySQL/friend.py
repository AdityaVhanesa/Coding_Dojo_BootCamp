from connection import SQL


class Friend:

    dataBase = 'FLASK_DB_TEST'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.__db = 'FLASK_DB_TEST'

    @classmethod
    def all(cls):
        query = "SELECT * FROM friends;"
        results = SQL(cls.dataBase).query(query)
        friends = []
        for friend in results:
            friends.append(cls(friend))

        return friends

    @classmethod
    def add(cls, data):
        query = 'INSERT INTO friends (first_name, last_name) VALUE ( %(f_name)s, %(l_name)s );'
        return SQL(cls.dataBase).query(query, data)
