class Monster:
    def __init__(self, health, energy, damage):
        self.health = health
        self.energy = energy
        self.damage = damage

class Scorpion(Monster):
    poison_damage = 10
    def __init__(self, health, energy, damage = poison_damage):
        super().__init__(health, energy, damage)

monster = Monster(100, 60, 20)
scorpion = Scorpion(100, 60)

print(scorpion.__dict__)

        
