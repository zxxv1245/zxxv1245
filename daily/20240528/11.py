class Zergling :
    def __init__(self):
        self.hp = 80
        self.mana = 200

    def attack(self):
        self.hp += 1
        self.mana -= 10

    def move(self):
        self.hp -= 10
        self.mana += 5

    def status(self):
        print(f'hp = {self.hp}')
        print(f'mana = {self.mana}')

Zergling1 = Zergling()
Zergling2 = Zergling()
Zergling1.attack()
Zergling2.move()
Zergling1.status()
Zergling2.status()