from dictionaries import start_weapon
from classes.Player import Player

class Guerrier(Player):
    def __init__(self):
        super().__init__()
        self.current_weapon = start_weapon["épée"]["attack"]         #permet de stocker l'attaque de l'arme actuelle
        self.health = 750
        self.max_health = 750
        self.fury = 0
        self.attack = 150 + self.current_weapon
        self.max_attack = 150 + self.current_weapon
        self.strenght = 35
        self.speed = 10
        self.inventory = [start_weapon["épée"]["name"]]       #permet de stocker l'arme dans l'inventaire du joueur
        self.luck = 50

    def level_up(self):
        super().level_up()
        self.strenght += 2.5
        