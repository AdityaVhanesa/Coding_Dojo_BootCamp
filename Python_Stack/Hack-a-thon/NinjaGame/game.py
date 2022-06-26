from classes.pirate import Pirate
from classes.ninja import Ninja
from time import  sleep

michelangelo = Ninja("Hathori", 5, 10)
jack_sparrow = Pirate("Jack Sparrow", 3, 12)

count = 0
while michelangelo.health > 0 and jack_sparrow.health > 0:
    count += 1
    if not count % michelangelo.speed:
        michelangelo.attackDir[michelangelo.randomAttack()](jack_sparrow)
        jack_sparrow.show_health()

    if not count % jack_sparrow.speed:
        jack_sparrow.attackDir[jack_sparrow.randomAttack()](michelangelo)
        michelangelo.show_health()

    sleep(1)


if michelangelo.health > 0:
    print("Ninja Wins")
elif jack_sparrow.health > 0:
    print("Piret Wins")
else:
    print("Match ties")
