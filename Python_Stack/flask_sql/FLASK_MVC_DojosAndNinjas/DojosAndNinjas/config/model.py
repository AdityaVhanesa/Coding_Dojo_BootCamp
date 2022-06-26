from .connection import SQL


class Model:

    def __init__(self, data):
        pass

    @classmethod
    def getAll(cls):
        query = f"SELECT * FROM {cls.tableName()};"
        results = SQL(cls.dataBase()).query(query)

        if not results:
            return []

        users = []
        for user in results:
            users.append(cls(user))

        return users

    @classmethod
    def save(cls, data):
        query = f'INSERT INTO {cls.tableName()}(first_name, last_name, email) VALUE (%(first_name)s, %(last_name)s, %(email)s);'
        return SQL(cls.dataBase()).query(query, data)

    @classmethod
    def getById(cls, data):
        query = f'SELECT * FROM {cls.tableName()} WHERE id = %(id)s;'
        result = SQL(cls.dataBase()).query(query, data)
        if result:
            return cls(result[0])

    @classmethod
    def removeById(cls, data):
        query = f"DELETE FROM {cls.tableName()} WHERE id = %(id)s;"
        SQL(cls.dataBase()).query(query, data)

    @classmethod
    def updateById(cls, data):
        query = f"UPDATE {cls.tableName()} SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        SQL(cls.dataBase()).query(query, data)

    @classmethod
    def dataBase(cls):
        pass

    @classmethod
    def tableName(cls):
        pass
