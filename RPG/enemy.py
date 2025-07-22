from character import Character
import random

class Enemy(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)

    def taunt(self):
        print(f"{self.name} : 'You won't survive for long!'")

    def deal_damage(self):
        damage = random.randint(self.attack - 2, self.attack + 2)
        return max(0, damage)
