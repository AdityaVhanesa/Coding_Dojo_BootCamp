import datetime

from flask import flash


class ReportForm:
    def __init__(self, post):
        self.location = post.get("location")
        self.description = post.get("description")
        self.date = post.get("date")
        self.numberOfSasquatches = post.get("number_of_sasquatch")

    def __str__(self):
        return f"{self.location} | {self.description} | {self.date} | {self.numberOfSasquatches}"

    def isValid(self):
        validFlag = True
        validFlag = self.validateLocation() and validFlag
        validFlag = self.validateDescription() and validFlag
        validFlag = self.validateDate() and validFlag
        validFlag = self.validateNumberOfSasquatches() and validFlag
        return validFlag

    def validateLocation(self):
        if self.location:
            return True
        flash("Missing", "location_error")
        return False

    def validateDescription(self):
        if self.description:
            return True
        flash("Missing", "description_error")
        return False

    def validateDate(self):
        if self.date:
            return True
        flash("Missing", "date_error")
        return False

    def validateNumberOfSasquatches(self):
        if self.numberOfSasquatches:
            if int(self.numberOfSasquatches) >= 1:
                return True

            flash("Minimum 1 required", "number_error")
            return False

        flash("Missing", "number_error")
        return False

    def cleanDate(self):
        dateList = self.date.split("-")
        self.date = datetime.datetime(int(dateList[0]), int(dateList[1]), int(dateList[2]))

    def cleanData(self):
        self.cleanDate()
        return {
            "location": self.location,
            "description": self.description,
            "created_at": self.date,
            "number_sasquatches": int(self.numberOfSasquatches)
        }
