from classes.Player import Player
from dictionaries import start_weapon

class Mage(Player):
    
    def __init__(self):
        super().__init__()
        self.current_weapon = start_weapon["baton magique"]["attack"]
        self.health = 550
        self.max_health = 550
        self.mana = 100
        self.max_mana = 100
        self.attack = 30 + self.current_weapon
        self.max_attack = 30 + self.current_weapon
        self.intelligence = 20
        self.speed = 12
        self.inventory = [start_weapon["baton magique"]["name"]]
        self.luck = 60
        

    def level_up(self):
        super().level_up()
        self.mana = self.max_mana
        self.intelligence += 2.5
