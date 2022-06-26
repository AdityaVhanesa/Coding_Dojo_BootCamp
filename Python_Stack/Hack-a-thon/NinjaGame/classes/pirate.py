from .player import Player


class Pirate(Player):

    def __init__(self, name, speed, strength):
        super().__init__(name, speed, strength)
        self.attackDir = {
            1: self.attack,
            2: self.special_attack,
            3: self.sward_swing
        }

    def special_attack(self, ninja):
        print("Pirate is performing the attack spree\n")
        for _ in range(4):
            self.attack(ninja)

    @staticmethod
    def sward_swing(ninja):
        print("Sward attack\n")
        ninja.health -= 2


