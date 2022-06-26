from Library.config.connection import SQL
from Library.config.dateTime import dateTime
from Library.models import books


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = dateTime(data['created_at'])
        self.updated_at = dateTime(data['updated_at'])
        self.books = data['books']

    @classmethod
    def dataBase(cls):
        return 'books_schema'

    @classmethod
    def tableName(cls):
        return 'authors'

    @classmethod
    def save(cls, data):
        query = f'INSERT INTO {cls.tableName()}(name) VALUE (%(name)s);'
        return SQL(cls.dataBase()).query(query, data)

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM authors;"
        return SQL(cls.dataBase()).query(query)

    @classmethod
    def getById(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        return SQL(cls.dataBase()).query(query, data)

    @classmethod
    def getAllBooks(cls, data):
        query = "SELECT  * " \
                "FROM books_has_authors " \
                "JOIN books " \
                "ON books_has_authors.book_id = books.id " \
                "JOIN authors " \
                "ON books_has_authors.author_id = authors.id WHERE authors.id = %(id)s;"
        results = SQL(cls.dataBase()).query(query, data)
        temp = []
        for row in results:
            temp.append(
                books.Book({
                    "id": row['book_id'],
                    "title": row['title'],
                    "num_of_pages": row['num_of_pages'],
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at']
                })
            )
        authorObject = cls({
            "id": results[0]['authors.id'],
            "name": results[0]['name'],
            "created_at": results[0]['authors.created_at'],
            "updated_at": results[0]['authors.updated_at'],
            "books": temp
        })
        return authorObject
