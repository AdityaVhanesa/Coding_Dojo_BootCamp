from random import randint


class Player:

    def __init__(self, name, speed, strength):
        self.life = 100
        self.name = name
        self.speed = speed
        self.strength = strength

    @property
    def health(self):
        return self.life

    @health.setter
    def health(self, number):
        if number > self.health:
            self.life = 0
        else:
            self.life = number

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def show_health(self):
        print(f"Name: {self.name}  |  Health: {self.health}")
        return self

    def attack(self, enemy):
        enemy.health -= self.strength

    @staticmethod
    def randomAttack():
        return randint(1, 3)
