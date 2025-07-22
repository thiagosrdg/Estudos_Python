class Item:

    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, target):
        print(f"{target.name} used {self.name}!")
        self.effect(target)

    def __str__(self):
        return self.name
        