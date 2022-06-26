from DojosAndNinjas.config.dateTime import dateTime
from DojosAndNinjas.config.model import Model
from DojosAndNinjas.config.connection import SQL


class Dojo(Model):

    def __init__(self, data):
        super().__init__(data)
        self.id = data['id']
        self.name = data['name']
        self.created_at = dateTime(data['created_at'])
        self.updated_at = dateTime(data['updated_at'])

    @classmethod
    def dataBase(cls):
        return "dojos_and_ninjas_schemas"

    @classmethod
    def tableName(cls):
        return "dojos"

    @classmethod
    def save(cls, data):
        query = f'INSERT INTO {cls.tableName()}(name) VALUE (%(name)s);'
        return SQL(cls.dataBase()).query(query, data)

    @classmethod
    def getByName(cls, data):
        query = f'SELECT * FROM  {cls.tableName()} WHERE name = %(name)s'
        result = SQL(cls.dataBase()).query(query, data)
        if result:
            return cls(result[0])