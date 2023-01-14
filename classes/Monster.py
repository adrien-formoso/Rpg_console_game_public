import random
from dictionaries import monsters

class Monster():
    def __init__(self, *args):
        if len(args) == 0:
            self.type = random.choice(list(monsters)) # CHOISI UN MONSTRE ALEATOIRE DE LA LISTE 
            self.health = monsters[self.type]["health"] # SELECTIONNE LES PV DU MONSTRE ALEATOIRE
            self.attack = monsters[self.type]["attack"] # SELECTIONNE L ATTAQUE DU MONSTRE ALEATOIRE
            self.speed = monsters[self.type]["speed"] # SELECTIONNE LA VITESSE DU MONSTRE ALEATOIRE
            self.xp = monsters[self.type]["xp"] # SELECTIONNE L XP DU MONSTRE ALEATOIRE
            self.loot = monsters[self.type]["loots"] # SELECTIONNE LES LOOTS DU MONSTRE ALEATOIRE
            self.is_random = True   

        else:
            self.type = args[0]
            self.health = args[1]
            self.attack = args[2]
            self.speed = args[3]
            self.xp = args[4]
            self.loot = args[5]
            self.is_random = False