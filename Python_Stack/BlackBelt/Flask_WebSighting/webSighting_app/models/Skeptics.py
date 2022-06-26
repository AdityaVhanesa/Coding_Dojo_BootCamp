from flask import flash

from webSighting_app.config.connection import SQL
from webSighting_app.models import Users, Sightings
from .CreateDate import createDate
from .UpdateDate import updateDate


class Skeptic:
    dataBase = "Sasquatch_Websighting"

    def __init__(self, data):
        self.id = data['id']
        self.isSkeptical = data['isSkeptical']
        self.isBeliever = data['isBeliever']
        self.created_at = createDate(data['created_at'])
        self.updated_at = updateDate(data['updated_at'])
        self.user = self.__fetchUserObject(data['users_id'])
        self.sighting = self.__fetchSightingObject(data['sightings_id'])

    @classmethod
    def add(cls, data):
        query = 'INSERT INTO ' \
                'skeptics(isSkeptical, isBeliever, sightings_id, users_id) ' \
                'VALUE (%(isSkeptical)s, %(isBeliever)s, %(sightings_id)s, %(users_id)s );'
        SQL(cls.dataBase).query(query, data)
        return True

    @classmethod
    def modify(cls, data):
        query = 'UPDATE skeptics ' \
                'SET isSkeptical=%(isSkeptical)s, isBeliever=%(isBeliever)s ' \
                'WHERE sightings_id=%(sightings_id)s AND users_id=%(users_id)s;'
        SQL(cls.dataBase).query(query, data)
        return True

    @classmethod
    def getById(cls, data):
        query = "SELECT * FROM skeptics WHERE id = %(id)s;"
        result = SQL(cls.dataBase).query(query, data)
        if result:
            return cls(result[0])

        return False

    @classmethod
    def getBySightingsId(cls, data):
        query = "SELECT * FROM skeptics WHERE sightings_id = %(sightings_id)s;"
        result = SQL(cls.dataBase).query(query, data)
        objectList = []
        if result:
            for record in result:
                objectList.append(cls(record))
                return objectList

        return []

    @classmethod
    def countSkepticsOnSighting(cls, data):
        query = "SELECT COUNT(id) FROM skeptics WHERE sightings_id=%(sightings_id)s AND isSkeptical = 1;"
        result = SQL(cls.dataBase).query(query, data)
        if result:
            return result[0]["COUNT(id)"]
        return 0

    @classmethod
    def getByUserId_SightingId(cls, data):
        query = "SELECT * FROM skeptics WHERE sightings_id=%(sightings_id)s AND users_id=%(users_id)s;"
        result = SQL(cls.dataBase).query(query, data)
        objectList = []
        if result:
            for record in result:
                objectList.append(cls(record))
            return objectList[0]
        return []

    @classmethod
    def removeByUserId_SightingId(cls, data):
        query = "DELETE FROM skeptics WHERE users_id = %(users_id)s AND sightings_id = %(sightings_id)s;"
        SQL(cls.dataBase).query(query, data)

    def __fetchUserObject(self, value):
        return Users.User.getUserById({"id": value})

    def __fetchSightingObject(self, value):
        return Sightings.Sighting.getById({"id": value})
