from DojosAndNinjas.config.connection import SQL
from DojosAndNinjas.config.dateTime import dateTime
from DojosAndNinjas.config.model import Model
from .dojos import Dojo


class Ninja(Model):
    def __init__(self, data):
        super().__init__(data)
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = dateTime(data['created_at'])
        self.updated_at = dateTime(data['updated_at'])
        self.relatedDojo = Dojo.getById({"id": data['id']})

    @classmethod
    def dataBase(cls):
        return "dojos_and_ninjas_schemas"

    @classmethod
    def tableName(cls):
        return "ninjas"

    @classmethod
    def save(cls, data):
        query = f'INSERT INTO {cls.tableName()}(first_name, last_name, age, dojo_id ) VALUE (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        return SQL(cls.dataBase()).query(query, data)

    @classmethod
    def getByDojoID(cls, data):
        query = f'SELECT * FROM {cls.tableName()} WHERE dojo_id = %(dojo_id)s;'
        results = SQL(cls.dataBase()).query(query, data)
        if not results:
            return []

        users = []
        for user in results:
            users.append(cls(user))

        return users
