from player import Player
from enemy import Enemy

class Battle:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def turn(self):
        print("\n---New Battle Begins---")
        input("Press enter to attack\n")

        damage = self.player.deal_damage()
        self.enemy.take_damage(damage)

        if not self.enemy.is_alive():
            print(f"{self.enemy.name} is dead!")
            return
        
        enemy_damage = self.enemy.deal_damage()
        self.player.take_damage(enemy_damage)

        if not self.player.is_alive():
            print(f"{self.player.name} is dead!")
