from player import Player
from enemy import Enemy
from battle import Battle
from items import Item

def heal_effect(character):
    damage = 20
    character.hp += damage
    print(f"{character.name} recovered {damage} HP! Now has {character.hp} HP.")

if __name__ == "__main__":
    hero = Player("Hero", hp=100, attack=20)
    boss = Enemy("Boss", hp=80, attack=15)

    potion = Item("Health Potion", heal_effect)
    hero.add_item(potion)
    hero.use_item("Health Potion")

    fight = Battle(hero, boss)

    while hero.is_alive() and boss.is_alive():
        fight.turn()

    print("\n End Game!")