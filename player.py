from character import Character

class Player(Character):
    def __init__(self, name, hp, attack): 
        super().__init__(name, hp, attack)
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} add to inventory.")

    def show_inventory(self):
        if self.inventory:
            print(f"Inventory: {self.inventory}")
        else:
            print(f"The inventory is empty.")

    def use_item(self, item_name):
        for item in self.inventory:
            if hasattr(item, 'name') and item.name == item_name:
                if hasattr(item, 'effect'):
                    item.effect(self)
                    self.inventory.remove(item)
                    print(f"{item_name} used.")
                    return
        print(f"Item '{item_name}' not found in inventory.")