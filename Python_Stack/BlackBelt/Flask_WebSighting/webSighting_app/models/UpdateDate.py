class updateDate:
    def __init__(self, dateTime):
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.dateTime = dateTime

    def __str__(self):
        return f"{self.days[self.dateTime.weekday()]} {self.dateTime.day}, {self.dateTime.year} at {self.dateTime.time()}"