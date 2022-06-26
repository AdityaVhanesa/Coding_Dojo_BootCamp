from flask import flash
from webSighting_app.models.CreateDate import createDate
from webSighting_app.config.connection import SQL
from webSighting_app.models import Users
from webSighting_app.models import Skeptics
from .CreateDate import createDate
from .UpdateDate import updateDate


class Sighting:
    dataBase = "Sasquatch_Websighting"

    def __init__(self, data):
        self.id = data["id"]
        self.location = data["location"]
        self.description = data["description"]
        self.number = data["number_sasquatches"]
        self.skeptics = None
        self.numberOfSkeptics = self.__fetchSkeptics()
        self.created_at = createDate(data["created_at"])
        self.user = self.__fetchUserObject(data["users_id"])

    @classmethod
    def add(cls, data):
        query = 'INSERT INTO ' \
                'sightings(location, description, number_sasquatches, users_id, created_at) ' \
                'VALUES (%(location)s, %(description)s, %(number_sasquatches)s, %(users_id)s, %(created_at)s);'
        SQL(cls.dataBase).query(query, data)
        return True

    @classmethod
    def modify(cls, data):
        query = 'UPDATE sightings ' \
                'SET location = %(location)s, description = %(description)s, number_sasquatches = %(number_sasquatches)s, created_at = %(created_at)s ' \
                'WHERE id = %(id)s;'
        SQL(cls.dataBase).query(query, data)
        return True

    @classmethod
    def getById(cls, data):
        query = "SELECT * FROM sightings WHERE id=%(id)s;"
        result = SQL(cls.dataBase).query(query, data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM sightings;"
        result = SQL(cls.dataBase).query(query)
        objectList = []
        if result:
            for record in result:
                objectList.append(cls(record))
            return objectList
        return []

    @classmethod
    def removeById(cls, data):
        query = "DELETE FROM sightings WHERE id = %(sightings_id)s"
        SQL(cls.dataBase).query(query, data)
        Skeptics.Skeptic.removeByUserId_SightingId(data)

    def __fetchUserObject(self, value):
        return Users.User.getUserById({"id": value})

    def __fetchSkeptics(self):
        return Skeptics.Skeptic.countSkepticsOnSighting({"sightings_id": self.id})

    def fetchSkepticsObject(self):
        self.skeptics = Skeptics.Skeptic.getBySightingsId({"sightings_id": self.id})
        return self.skeptics

    def __str__(self):
        return f"{self.location} - {self.created_at}"