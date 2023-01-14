from dictionaries import start_weapon
from classes.Player import Player

class Guerrier(Player):
    def __init__(self):
        super().__init__()
        self.current_weapon = start_weapon["épée"]["attack"]
        self.health = 15
        self.max_health = 15
        self.fury = 0
        self.attack = 400 + self.current_weapon
        self.max_attack = 400 + self.current_weapon
        self.strenght = 35
        self.speed = 10
        self.inventory = [start_weapon["épée"]["name"]]
        self.luck = 50

    def level_up(self):
        super().level_up()
        self.strenght += 2.5
        