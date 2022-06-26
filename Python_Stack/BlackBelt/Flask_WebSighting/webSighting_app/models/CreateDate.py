class createDate:
    def __init__(self, dateTime):
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September",
                       "October", "November", "December"]

        self.dateTime = dateTime
        self.numberFormate = True
        self.formFormate = False

    def __str__(self):
        if self.numberFormate:
            return f"{self.dateTime.month}/{self.dateTime.day}/{self.dateTime.year}"

        if self.formFormate:
            return f"{self.dateTime.year}-{self.getMonth()}-{self.getDay()}"

        return f"{self.months[self.dateTime.month]} {self.dateTime.day}, {self.dateTime.year}"

    def toggleFormate(self):
        self.numberFormate = not self.numberFormate
        self.formFormate = False
        return ""

    def setFormFormate(self):
        self.numberFormate = False
        self.formFormate = True
        return ""

    def unSetFormFormate(self):
        self.numberFormate = True
        self.formFormate = False
        return ""

    def getDay(self):
        if self.dateTime.day < 10:
            return int(f"0{self.dateTime.day}")

        return self.dateTime.day

    def getMonth(self):
        if self.dateTime.month < 10:
            return f"0{self.dateTime.month}"

        return self.dateTime.Month
