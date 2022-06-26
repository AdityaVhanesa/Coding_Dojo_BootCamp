from Library.config.connection import SQL
from Library.config.dateTime import dateTime


class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data['title']
        self.pages = data['num_of_pages']
        self.created_at = dateTime(data['created_at'])
        self.updated_at = dateTime(data['updated_at'])

    @classmethod
    def dataBase(cls):
        return 'books_schema'

    @classmethod
    def tableName(cls):
        return 'books'

    @classmethod
    def save(cls, data):
        query = f'INSERT INTO {cls.tableName()}(name) VALUE (%(name)s);'
        return SQL(cls.dataBase()).query(query, data)
