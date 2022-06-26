class Pet:
    def __init__(self, pet):
        self._name = pet["name"]
        self._type = pet["kind"]
        self._trick = pet["trick"]
        self._health = 100
        self._energy = 100
        self.noise_sound = pet["noise"]

    @property
    def health(self):
        if self._health < 20:
            print(f"Your lovely pet {self._name} needs food.")
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value

    @property
    def energy(self):
        if self._energy < 20:
            print(f"Your lovely pet {self._name} needs to rest")
        return self._energy

    @energy.setter
    def energy(self, value):
        if value < 0:
            self._energy = 0
        else:
            self._energy = value

    def sleep(self):
        print(f"Shhh your lovely pet {self._name} is sleeping")
        self.energy += 25
        return self

    def eat(self):
        print(f"Your lovely pet {self._name} is eating")
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        print(f"Have a great play with your pet {self._name}")
        self.health += 5

    def noise(self):
        print(f"{self.noise_sound}...!" * 3)

    def walk(self):
        """Must be overrriden"""
        raise NotImplemented

    def feed(self):
        raise NotImplemented

    def bathe(self):
        raise NotImplemented


class Ninja(Pet):
    def __init__(self, ninja, pet):
        super().__init__(pet)
        self.first_name = ninja["first_name"]
        self.last_name = ninja["last_name"]

    def walk(self):
        self.play()
        return self

    def feed(self):
        self.eat()
        return self

    def bathe(self):
        self.noise()
        return self


Hathori = Ninja(
    {
        "first_name": "Hathori",
        "last_name": "Kawasaki",
    },
    {
        "name": "Tommy",
        "kind": "BullDog",
        "trick": "Stading _ Barking",
        "noise": "Bark"

    }
)

Sinjo = Ninja(
    {
        "first_name": "Sinjo",
        "last_name": "Kawasaki",
    },
    {
        "name": "Lammy",
        "kind": "CAT",
        "trick": "Leaping",
        "noise": "Meww"

    }
)

Hathori.feed().walk().bathe()
Sinjo.feed().walk().bathe()
