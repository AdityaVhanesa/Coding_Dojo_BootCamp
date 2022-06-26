class Under_Score:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])

        return iterable

    def find(self, iterable, callback):
        for value in iterable:
            if callback(value):
                return value
        return False

    def filter(self, iterable, callback):
        tempArray = []
        for value in iterable:
            if callback(value):
                tempArray.append(value)

        return tempArray

    def reject(self, iterable, callback):
        tempArray = []
        for value in iterable:
            if not callback(value):
                tempArray.append(value)

        return tempArray


_ = Under_Score()
print(_.map([1, 2, 3], lambda x: x * 2))
print(_.find([1, 2, 3, 4, 5, 6], lambda x: x > 4))
print(_.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
print(_.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
