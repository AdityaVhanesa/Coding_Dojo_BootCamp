from .player import Player


class Ninja(Player):

    def __init__(self, name, speed, strength):
        super().__init__(name, speed, strength)
        self.attackDir = {
            1: self.attack,
            2: self.special_attack,
            3: self.punch_and_kick
        }

    def special_attack(self, pirate):
        print("Ninja is performing the attack streak\n")
        for _ in range(3):
            self.attack(pirate)

    @staticmethod
    def punch_and_kick(pirate):
        print("Puching and kicking the pirate\n")
        pirate.health -= 3

