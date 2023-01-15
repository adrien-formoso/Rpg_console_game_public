from dictionaries import start_weapon
from classes.Player import Player

class Chasseur(Player):         
    def __init__(self):
        super().__init__()
        self.current_weapon = start_weapon["arc courbé"]["attack"]     #permet de stocker l'attaque de l'arme actuelle
        self.health = 600
        self.max_health = 600
        self.energy = 100
        self.max_energy = 100
        self.attack = 35 + self.current_weapon
        self.max_attack = 35 + self.current_weapon
        self.agility = 20
        self.speed = 15
        self.inventory = [start_weapon["arc courbé"]["name"]]     #permet de stocker l'arme dans l'inventaire du joueur
        self.luck = 70

    def level_up(self):
        super().level_up()
        self.energy = self.max_energy
        self.agility += 2.5
        