import random
import sys
import time
import os
from colorama import init, Fore

def quete_annexe():
    global current_quest
    
    global current_quest_description
    if current_quest == None:
        current_quest = random.choice(list(quests))
        current_quest_description = quests[current_quest]["description"]

        print (current_quest_description)

    else:
        print (f'Vous avez déjà une quête en cours ! \nPour rappel : {current_quest_description}')


################################################### QUETES
######################################################################################################
################################################### CLASSES

class Guerrier:
    def __init__(self):
        self.current_weapon = start_weapon["épée"]["attack"]
        self.health = 750
        self.fury = 0
        self.attack = 40 + self.current_weapon
        self.strenght = 35
        self.speed = 10
        self.xp = 0
        self.location = 'start'
        self.level = 1
        self.inventory = [start_weapon["épée"]["name"]]
        self.money = 0
        self.luck = 50

    def level_up(self):
        self.health += 25
        self.attack += 5
        self.strenght += 2.5
        self.speed += 1
        self.xp -= 100
        self.level += 1
        print (f"Level up !  Vous avez atteint le niveau {self.level} !" )

class Mage:
    def __init__(self):
        self.health = 550
        self.mana = 100
        self.attack = 30
        self.intelligence = 20
        self.speed = 12
        self.xp = 0
        self.location = 'start'
        self.level = 1
        self.inventory = []
        self.money = 0
        self.luck = 60

    def level_up(self):
        self.health += 25
        self.mana += 10
        self.attack += 5
        self.intelligence += 2.5
        self.speed += 1
        self.xp -= 100
        self.level += 1
        print (f"Level up !  Vous avez atteint le niveau {self.level} !" )

class Chasseur:
    def __init__(self):
        self.health = 600
        self.energy = 100
        self.attack = 35 + current_weapon
        self.agility = 20
        self.speed = 15
        self.xp = 0
        self.location = 'start'
        self.level = 1
        current_weapon = start_weapon["arc courbé"]
        self.inventory = [start_weapon["arc courbé"]]
        self.money = 0
        self.luck = 70

    def level_up(self):
        self.health += 25
        self.energy += 10
        self.attack += 5
        self.agility += 2.5
        self.speed += 1
        self.xp -= 100
        self.level += 1
        print (f"Level up !  Vous avez atteint le niveau {self.level} !" )

def set_player_attribute():
    
    name = "Veuillez créer votre pseudo:\n"
    for character in name:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    name = input("> ")
    while len(name) > 15 or len(name) < 4:
        print("Votre pseudo doit être compris entre 4 et 15 caractères")
        name = input("> ")
    
    print(f"Bienvenue {name} ! \n")
    print("~~~~~~ Choix de la classe ~~~~~~ \n  Guerrier     Mage     Chasseur \n")

    global player_class
    player_class = input("> ")
    while player_class.lower() not in ["guerrier","mage","chasseur"]:
        print("Veuillez sélectionner une classe")
        player_class = input("> ")
    if player_class.lower() == "guerrier":
        player_class = Guerrier
    elif player_class.lower() == "mage":
        player_class = Mage()
    elif player_class.lower() == "chasseur":
        player_class = Chasseur()



################################################### CLASSES
######################################################################################################
################################################### VILAGES DIVERS

shop ={    
    "épée améliorée":{"name":"épée améliorée","attack":30, "price": 50},
    "baton magique amélioré":{"name":"baton magique amélioré","attack":30, "price": 50 }, 
    "arc courbé amélioré":{"name":"arc courbé amélioré","attack":30, "price": 50},
    "potion de soin":{"heal":50, "price":20},
    "potion de force":{"attack":50, "price":30},
    "potion de mana":{"mana":40, "price":20},
    "potion de vitesse":{"speed":5,"price":30}
}
################################################### VILAGES DIVERS
######################################################################################################
################################################### COMBAT



monsters = {
    "loup":{"health":100,"attack":30, "speed":8, "xp": 10, 
        "loots":{"canine" : 5, "peau de loup":20}},

    "ours":{"health":300, "attack":50, "speed": 5, "xp":20,
        "loots":{"pâte d'ours": 5,"fourure d'ours" : 30}},

    "sanglier":{"health":130, "attack":35, "speed": 7, "xp":15,
        "loots":{"défense brisée":5,"peau de sanglier":20}},

    "rat":{"health":80, "attack":20, "speed": 10,"xp":5,
        "loots":{"griffe de rat":5,"queue de rat":15}},

    "araignée": {"health":150, "attack":40, "speed": 8, "xp":17.5,
        "loots":{"pâte d'araignée":5,"soie":20}},

    "bandit": {"health":250, "attack":45, "speed": 12, "xp":25,
        "loots":{"foulard":5,"dague brisée":20}},
}

random_monster = random.choice(list(monsters)) # CHOISI UN MONSTRE ALEATOIRE DE LA LISTE 
random_monster_health = monsters[random_monster]["health"] # SELECTIONNE LES PV DU MONSTRE ALEATOIRE
random_monster_attack = monsters[random_monster]["attack"] # SELECTIONNE L ATTAQUE DU MONSTRE ALEATOIRE
random_monster_speed = monsters[random_monster]["speed"] # SELECTIONNE LA VITESSE DU MONSTRE ALEATOIRE
random_monster_xp = monsters[random_monster]["xp"] # SELECTIONNE L XP DU MONSTRE ALEATOIRE
random_monster_loot = monsters[random_monster]["loots"] # SELECTIONNE LES LOOTS DU MONSTRE ALEATOIRE

def start_mage_combat():
    global random_monster_health
    print (f"Vous avez: {player_class.health} HP ----- Votre ennemi(e) à: {random_monster_health} HP")
    
    
    if player_class.speed <= random_monster_speed:
        print (f"Votre vitesse est de : {player_class.speed} ----- Celle de votre ennemi(e) est de : {random_monster_speed}")
        print ("L'ennemi(e) attaque en premier !")
        player_class.health -= random_monster_attack
        print (f"L'ennemi(e) vous inflige {random_monster_attack} points de dégât ! Il vous reste {player_class.health} HP")
    
    else:
        print (f"Votre vitesse est de : {player_class.speed} ----- Celle de votre ennemi(e) est de : {random_monster_speed}")
        print ("Vous attaquez en premier !")
    

    while player_class.health > 0 or random_monster_health > 0:
        if player_class.mana > 100:
            player_class.mana = 100
        if player_class.mana >= 20:
            print (f"Votre mana est de {player_class.mana}, souhaitez-vous lancer une boule de feu ? \n- oui ou - non ?")
            check_mana = input("> ")
            while check_mana not in ["oui","non"]:
                print("Veuillez répondre par oui ou par non")
                check_mana = input("> ")
            if check_mana == "oui":
                player_class.mana -= 20
                print("Bouuuule de feu !!!")
                player_attack = player_class.attack + player_class.intelligence
                random_monster_health -= player_attack
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {random_monster_health} HP')

            elif check_mana == "non":
                print ("Projectile de glace !")
                player_attack = player_class.attack
                random_monster_health -= player_attack
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {random_monster_health} HP')
                player_class.mana += 10

            if random_monster_health <= 0:
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                break
                    
            player_class.health -= random_monster_attack
            print (f"L'ennemi(e) vous inflige {random_monster_attack} points de dégât ! Il vous reste {player_class.health} HP")
            if player_class.health <= 0:
                print ("Vous succombez de vos blessures !!! \n Game over !")
                break
        else:
            print (f"Votre mana est de {player_class.mana}, vous n'avez pas assez pour lancer une boule de feu !")
            print ("Projectile de glace !")
            player_attack = player_class.attack
            random_monster_health -= player_attack
            print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {random_monster_health} HP')
            player_class.mana += 10
        
            if random_monster_health <= 0:
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                break

            player_class.health -= random_monster_attack
            print (f"L'ennemi(e) vous inflige {random_monster_attack} points de dégât ! Il vous reste {player_class.health} HP")
            
        if player_class.health <= 0:
            print ("Vous succombez de vos blessures !!! \n Game over !")
            break

    if random_monster_health <= 0:
        player_class.xp += random_monster_xp
        print (f"Vous obtenez {random_monster_xp} points d'expériences ! ")
        print (f"Vous êtes à {player_class.xp} / 100 points d'expériences pour le prochain niveau.")
        if player_class.xp > 100:
            player_class.level_up()
        
        loot = random.randint(0,100)
        if loot >= 25:
            player_loot = random.choice(list(random_monster_loot))
            print (f"Vous fouillez le cadavre et vous trouvez : {player_loot} \nL'objet a été ajouté à votre inventaire...")
            player_class.inventory.append(player_loot)
        else:
            print("Vous ne trouvez rien sur le cadavre")

def start_guerrier_combat():
    global random_monster_health
    player_class.fury = 0
    print (f"Vous avez: {player_class.health} HP ----- Votre ennemi(e) à: {random_monster_health} HP")
    
    
    if player_class.speed <= random_monster_speed:
        print (f"Votre vitesse est de : {player_class.speed} ----- Celle de votre ennemi(e) est de : {random_monster_speed}")
        print ("L'ennemi(e) attaque en premier !")
        player_class.health -= random_monster_attack
        print (f"L'ennemi(e) vous inflige {random_monster_attack} points de dégât ! Il vous reste {player_class.health} HP")
    
    else:
        print (f"Votre vitesse est de : {player_class.speed} ----- Celle de votre ennemi(e) est de : {random_monster_speed}")
        print ("Vous attaquez en premier !")
    

    while player_class.health > 0 or random_monster_health > 0:
        if player_class.fury >= 30:
            print (f"Votre furie est de {player_class.fury}, souhaitez-vous assainer un puissant coup ? \n- oui ou - non ?")
            check_fury = input("> ")
            while check_fury not in ["oui","non"]:
                print("Veuillez répondre par oui ou par non")
                check_fury = input("> ")
            if check_fury == "oui":
                player_class.fury -= 30
                print("Chaaarge !!!")
                player_attack = player_class.attack + player_class.strenght
                random_monster_health -= player_attack
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {random_monster_health} HP')

            elif check_fury == "non":
                print ("Coup d'épée !")
                player_attack = player_class.attack
                random_monster_health -= player_attack
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {random_monster_health} HP')
                player_class.fury += 20

            if random_monster_health <= 0:
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                break
                    
            player_class.health -= random_monster_attack
            print (f"L'ennemi(e) vous inflige {random_monster_attack} points de dégât ! Il vous reste {player_class.health} HP")
            if player_class.health <= 0:
                print ("Vous succombez de vos blessures !!! \n Game over !")
                break
        else:
            print (f"Votre furie est de {player_class.fury}, vous n'avez pas assez pour lancer un puissant coup !")
            print ("Coup d'épée !")
            player_attack = player_class.attack
            random_monster_health -= player_attack
            print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {random_monster_health} HP')
            player_class.fury += 20
        
            if random_monster_health <= 0:
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                break

            player_class.health -= random_monster_attack
            print (f"L'ennemi(e) vous inflige {random_monster_attack} points de dégât ! Il vous reste {player_class.health} HP")
            
        if player_class.health <= 0:
            print ("Vous succombez de vos blessures !!! \n Game over !")
            break
    if random_monster_health <= 0:
        player_class.xp += random_monster_xp
        print (f"Vous obtenez {random_monster_xp} points d'expériences ! ")
        print (f"Vous êtes à {player_class.xp} / 100 points d'expériences pour le prochain niveau.")
        if player_class.xp > 100:
            player_class.level_up()
        
        loot = random.randint(0,100)
        if loot >= 25:
            player_loot = random.choice(list(random_monster_loot))
            print (f"Vous fouillez le cadavre et vous trouvez : {player_loot} \nL'objet a été ajouté à votre inventaire...")
            player_class.inventory.append(player_loot)
        else:
            print("Vous ne trouvez rien sur le cadavre")

def start_chasseur_combat():
    global random_monster_health

    print (f"Vous avez: {player_class.health} HP ----- Votre ennemi(e) à: {random_monster_health} HP")
    
    
    if player_class.speed <= random_monster_speed:
        print (f"Votre vitesse est de : {player_class.speed} ----- Celle de votre ennemi(e) est de : {random_monster_speed}")
        print ("L'ennemi(e) attaque en premier !")
        player_class.health -= random_monster_attack
        print (f"L'ennemi(e) vous inflige {random_monster_attack} points de dégât ! Il vous reste {player_class.health} HP")
    
    else:
        print (f"Votre vitesse est de : {player_class.speed} ----- Celle de votre ennemi(e) est de : {random_monster_speed}")
        print ("Vous attaquez en premier !")
    

    while player_class.health > 0 or random_monster_health > 0:
        if player_class.energy > 100:
            player_class.energy = 100
        if player_class.energy >= 20:
            print (f"Votre énergie est de {player_class.energy}, souhaitez-vous lancer Flèches multiples ? \n- oui ou - non ?")
            check_energy = input("> ")
            while check_energy not in ["oui","non"]:
                print("Veuillez répondre par oui ou par non")
                check_energy = input("> ")
            if check_energy == "oui":
                player_class.energy -= 20
                print("Flèches multiples !!!")
                player_attack = player_class.attack + player_class.agility
                random_monster_health -= player_attack
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {random_monster_health} HP')

            elif check_energy == "non":
                print ("Tir de flèche !")
                player_attack = player_class.attack
                random_monster_health -= player_attack
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {random_monster_health} HP')
                player_class.energy += 5

            if random_monster_health <= 0:
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                break
                    
            player_class.health -= random_monster_attack
            print (f"L'ennemi(e) vous inflige {random_monster_attack} points de dégât ! Il vous reste {player_class.health} HP")
            if player_class.health <= 0:
                print ("Vous succombez de vos blessures !!! \n Game over !")
                break
        else:
            print (f"Votre énergie est de {player_class.energy}, vous n'avez pas assez pour lancer vos flèches multiples !")
            print ("Tir de flèche !")
            player_attack = player_class.attack
            random_monster_health -= player_attack
            print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {random_monster_health} HP')
            player_class.energy += 5
        
            if random_monster_health <= 0:
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                break

            player_class.health -= random_monster_attack
            print (f"L'ennemi(e) vous inflige {random_monster_attack} points de dégât ! Il vous reste {player_class.health} HP")
            
        if player_class.health <= 0:
            print ("Vous succombez de vos blessures !!! \n Game over !")
            break
    if random_monster_health <= 0:
        player_class.xp += random_monster_xp
        print (f"Vous obtenez {random_monster_xp} points d'expériences ! ")
        print (f"Vous êtes à {player_class.xp} / 100 points d'expériences pour le prochain niveau.")
        if player_class.xp > 100:
            player_class.level_up()
        
        loot = random.randint(0,100)
        if loot >= 25:
            player_loot = random.choice(list(random_monster_loot))
            print (f"Vous fouillez le cadavre et vous trouvez : {player_loot} \nL'objet a été ajouté à votre inventaire...")
            player_class.inventory.append(player_loot)
            print (player_class.inventory)
        else:
            print("Vous ne trouvez rien sur le cadavre")

################################################### COMBAT
######################################################################################################
################################################### MAP

def creation_liste_position_dispo(largeur):
  liste = []
  for i in range(0,largeur*largeur):
    liste.append(i)
  return liste

def generation_de_map(largeur):
  map = []
  for i in range(largeur*largeur):
    map.append("-")
  
  return map

def liste_du_nb_village(nb_villages):

  liste_nb_village = []
  for i in range(nb_villages):
    liste_nb_village.append(i+1)
  return liste_nb_village

def generateur_villages(largeur,nb_villages):

  liste_position_dispo = []

  map = generation_de_map(largeur)

  liste_position_dispo = creation_liste_position_dispo(largeur)
  

  for i in range(1,nb_villages+1):
    position = liste_position_dispo[random.randint(0,len(liste_position_dispo)-1)]
    liste_position_dispo.remove(position)
    map[position] = i

  return map

def dernien_chiffre_de_la_ligne(largeur):
  liste = []
  i = 1
  while i < largeur:
    liste.append(largeur*i-1)
    i = i + 1
  return liste

def ajout_foret_map(map,nb_villages,largeur):
  liste_des_nom_village = liste_du_nb_village(nb_villages)
  i = 0
  while i < largeur*largeur:
    if map[i] in liste_des_nom_village:
      pass
    elif i == 0: #si c'est la case tout en haut a gauche
      if map[i+1] not in liste_des_nom_village: #si la case à droite est vide
        if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
          if map[i+largeur+1] not in liste_des_nom_village: #si la case en dessous à droite est vide
            map[i] = "F"

    elif i == largeur-1: #si la case en haut à droite
      if map[i-1] not in liste_des_nom_village: #si la case à gauche est vide
        if map[i+largeur-1] not in liste_des_nom_village: #si la case en bas a gauche est vide
          if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
            map[i] = "F"

    elif i == largeur*largeur-largeur : #si c'est la case en bas a gauche
      if map[i-largeur] not in liste_des_nom_village: #si la case en haut est vide
        if map[i-largeur+1] not in liste_des_nom_village: #si la case en haut à droite est vide
          if map[i+1] not in liste_des_nom_village: #si la case à droite est vide
            map[i] = "F"
    
    elif i == largeur*largeur-1: #si c'est la case tout en bas à droite
      if map[i-largeur] not in liste_des_nom_village: #si la case en haut est vide
        if map[i-largeur-1] not in liste_des_nom_village: #si la case en haut à gauche est vide
          if map[i-1] not in liste_des_nom_village: #si la case à gauche est vide
            map[i] = "F"

    elif i%largeur == 0 : #si la case est sur la colonne a gauche
      if map[i-largeur] not in liste_des_nom_village: #si la case en haut est vide
        if map[i-largeur+1] not in liste_des_nom_village: #si la case en haut à droite est vide
          if map[i+1] not in liste_des_nom_village: #si la case à droite est vide
            if map[i+largeur+1] not in liste_des_nom_village: #si la case en dessous à droite est vide
              if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
                map[i] = "F"

    elif i in dernien_chiffre_de_la_ligne(largeur): #si la case est tout à droite
      if map[i-largeur] not in liste_des_nom_village: #si la case en haut est vide
        if map[i-largeur-1] not in liste_des_nom_village: #si la case en haut à gauche est vide
          if map[i-1] not in liste_des_nom_village: #si la case à gauche est vide
            if map[i+largeur-1] not in liste_des_nom_village: #si la case en bas à gauche est vide
              if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
                map[i] = "F"

    elif i>0 and i<largeur : #si la case est juste sur la premiere ligne
      if map[i-1] not in liste_des_nom_village: #si la case à gauche est vide
        if map[i+1] not in liste_des_nom_village: #si la case à droite est vide
          if map[i+largeur-1] not in liste_des_nom_village: #si la case en bas à gauche est vide
            if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
              if map[i+largeur+1] not in liste_des_nom_village: #si la case en dessous à droite est vide
                map[i] = "F"

    elif i >= largeur*largeur-largeur-1 and i <=largeur*largeur-2: #si la case est sur la dernière ligne
      if map[i-largeur+1] not in liste_des_nom_village: #si la case en haut à gauche est vide
        if map[i-largeur] not in liste_des_nom_village: #si la case en haut est vide
          if map[i-largeur-1] not in liste_des_nom_village: #si la case en haut à droite est vide
            if map[i-1] not in liste_des_nom_village: #si la case à gauche est vide
              if map[i+1] not in liste_des_nom_village: #si la case à droite est vide
                map[i] = "F"

    elif i > largeur-1 and i < largeur*largeur-largeur: #si la case est au centre
      if map[i-largeur+1] not in liste_des_nom_village: #si la case en haut à gauche est vide
        if map[i-largeur] not in liste_des_nom_village: #si la case en haut est vide
          if map[i-largeur-1] not in liste_des_nom_village: #si la case en haut à droite est vide
            if map[i-1] not in liste_des_nom_village: #si la case à gauche est vide
              if map[i+1] not in liste_des_nom_village: #si la case à droite est vide
                if map[i+largeur-1] not in liste_des_nom_village: #si la case en bas à gauche est vide
                  if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
                    if map[i+largeur+1] not in liste_des_nom_village: #si la case en dessous à droite est vide
                      map[i] = "F"
    i = i + 1
  return map


def creation_map(largeur,nb_villages):
  map = 0
  map = ajout_foret_map(generateur_villages(largeur,nb_villages),nb_villages,largeur)
  map = declaration_position_debut_aleaatoire(map,largeur)
  
  return map

def affichage_map(map,largeur):
  i = 0
  couleurs = [
    Fore.RED,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN]
  while i < largeur*largeur+2:
    couleur = random.choice(couleurs)
    if i%largeur == 0:
      print()
    if isinstance(map[i], int):
      if map[i] < 10:
        if i == map[-1]:
          print(Fore.YELLOW +str(map[i]),end = " ")
        else :
          print(couleur +str(map[i]),end = " ")

        
      else:
        if i == map[-1]:
          print(Fore.YELLOW +str(map[i]),end = "")
        else :
          print(couleur +str(map[i]),end = "")

    elif  map[i] == "-" or map[i] == "F" or map[i] == "f" or map[i] == "D":
      if i == map[-1]:
        if map[-1] == map[-2]:
          print(Fore.YELLOW +str(map[i]),end = " ")
        else :
          print(Fore.YELLOW + "X",end = " ")
      elif map[i] == "f":
        print(Fore.GREEN + str(map[i]),end = " ")
      elif map[i] == "D":
        print(Fore.RED + str(map[i]),end = " ")
      else:
        print(Fore.RESET + str(map[i]),end = " ")

    i += 1
  print("\n")

def liste_position_village(map):

  position_des_villages = []
  i = 0
  while i < len(map):
    if type(map[i]) is int:
      position_des_villages.append(i)
    i = i +1
  return position_des_villages

def declaration_position_debut_aleaatoire(map,largeur):
  
  position_joueur = liste_position_village(map)
  position_joueur = position_joueur[random.randint(0,len(position_joueur)-1)]

  position_donjon = position_disponible_donjon(map,largeur)
  position_donjon = position_donjon[random.randint(0,len(position_donjon)-1)]

  map.append(position_donjon)
  map.append(position_joueur)
  return map

def position_disponible_donjon(map,largeur):
  liste_position_disponible = []
  i = 0
  while i < largeur*largeur:
    if map[i] == "F":
      liste_position_disponible.append(i)
    i = i + 1

  return liste_position_disponible

def choix_de_direction():
  menu_deplacement()
  choix = input("Que voulez vous faire ? : ")
  while choix not in ["2","4","6","8"]:
    print("\nmerci de renseigner la bonne valeur\n")
    menu_deplacement()
    choix = input("Que voulez vous faire ? : ")
  return int(choix)
  
def verification_possibilite_deplacement(map,choix,largeur):
  position_acteulle = map[-1]
  if position_acteulle == 0: #si c'est la case tout en haut a gauche
    if choix in [6,2]:
      return True
    else:
      return False
  elif position_acteulle == largeur-1: #si la case en haut à droite
    if choix in [4,2]:
      return True
    else:
      return False
  elif position_acteulle == largeur*largeur-largeur : #si c'est la case en bas a gauche
    if choix in [8,6]:
      return True
    else:
      return False
  elif position_acteulle == largeur*largeur-1: #si c'est la case tout en bas à droite
    if choix in [4,8]:
      return True
    else:
      return False
  elif position_acteulle%largeur == 0 : #si la case est sur la colonne a gauche
    if choix in [8,6,2]:
      return True
    else:
      return False
  elif position_acteulle in dernien_chiffre_de_la_ligne(largeur): #si la case est tout à droite
    if choix in [8,4,2]:
      return True
    else:
      return False
  elif position_acteulle>0 and position_acteulle<largeur : #si la case est juste sur la premiere ligne
    if choix in [4,2,6]:
      return True
    else:
      return False
  elif position_acteulle >= largeur*largeur-largeur-1 and position_acteulle <=largeur*largeur-2: #si la case est sur la dernière ligne
    if choix in [4,8,6]:
      return True
    else:
      return False
  else: # si la position est au centre
    return True

def deplacement_du_joueur(map,largeur):
  choix = choix_de_direction()

  while not verification_possibilite_deplacement(map,choix,largeur):
    print("\nHors map. merci de rester dans la map\n")    
    choix = choix_de_direction()


  if choix == 8:
    map[-1] = map[-1] - largeur # vers le haut
  elif choix == 4:
    map[-1] = map[-1] - 1 # vers la gauche
  elif choix == 6:
    map[-1] = map[-1] + 1 # vers la droite
  else:
    map[-1] = map[-1] + largeur # vers le bas

  map = decouverte_map(map,largeur)

  return map

def decouverte_map(map,largeur):
  position_actuel = map[-1]
  position_donjon = map[-2]

  if position_actuel == 0: #si c'est la case tout en haut a gauche
    if map[position_actuel+1] == "F": # a droite
      map[position_actuel+1]  = "f"
    if map[position_actuel+largeur] == "F": # en bas
      map[position_actuel+largeur]  = "f"
    if map[position_actuel+largeur+1] == "F": # en bas a droite
      map[position_actuel+largeur+1] = "f"

  elif position_actuel == largeur-1: #si la case en haut à droite
    if map[position_actuel-1] == "F": # a gauche
      map[position_actuel-1]  = "f"
    if map[position_actuel+largeur-1] == "F": # en bas a gauche
      map[position_actuel+largeur-1] = "f"
    if map[position_actuel+largeur] == "F": # en bas
      map[position_actuel+largeur]  = "f"

  elif position_actuel == largeur*largeur-largeur : #si c'est la case en bas a gauche
    if map[position_actuel-largeur] == "F": # en haut
      map[position_actuel-largeur]  = "f"
    if map[position_actuel-largeur+1] == "F": # en haut a droite
      map[position_actuel-largeur+1] = "f"
    if map[position_actuel+1] == "F": # a droite
      map[position_actuel+1]  = "f"
    
  elif position_actuel == largeur*largeur-1: #si c'est la case tout en bas à droite
    if map[position_actuel-largeur] == "F": # en haut
      map[position_actuel-largeur]  = "f"
    if map[position_actuel-largeur-1] == "F": # en haut a gauche
      map[position_actuel-largeur-1] = "f"
    if map[position_actuel-1] == "F": # a gauche
      map[position_actuel-1]  = "f"

  elif position_actuel%largeur == 0 : #si la case est sur la colonne a gauche
    if map[position_actuel-largeur] == "F": # en haut
      map[position_actuel-largeur]  = "f"
    if map[position_actuel-largeur+1] == "F": # en haut a droite
      map[position_actuel-largeur+1] = "f"
    if map[position_actuel+1] == "F": # a droite
      map[position_actuel+1]  = "f"
    if map[position_actuel+largeur+1] == "F": # en bas a droite
      map[position_actuel+largeur+1] = "f"
    if map[position_actuel+largeur] == "F": # en bas
      map[position_actuel+largeur]  = "f"

  elif position_actuel in dernien_chiffre_de_la_ligne(largeur): #si la case est tout à droite
    if map[position_actuel-largeur] == "F": # en haut
      map[position_actuel-largeur]  = "f"
    if map[position_actuel-largeur-1] == "F": # en haut a gauche
      map[position_actuel-largeur-1] = "f"
    if map[position_actuel-1] == "F": # a gauche
      map[position_actuel-1]  = "f"
    if map[position_actuel+largeur-1] == "F": # en bas a gauche
      map[position_actuel+largeur-1] = "f"
    if map[position_actuel+largeur] == "F": # en bas
      map[position_actuel+largeur]  = "f"

  elif position_actuel>0 and position_actuel<largeur : #si la case est juste sur la premiere ligne
    if map[position_actuel-1] == "F": # a gauche
      map[position_actuel-1]  = "f"
    if map[position_actuel+1] == "F": # a droite
      map[position_actuel+1]  = "f"
    if map[position_actuel+largeur-1] == "F": # en bas a gauche
      map[position_actuel+largeur-1] = "f"
    if map[position_actuel+largeur] == "F": # en bas
      map[position_actuel+largeur]  = "f"
    if map[position_actuel+largeur+1] == "F": # en bas a droite
      map[position_actuel+largeur+1] = "f"

  elif position_actuel >= largeur*largeur-largeur-1 and position_actuel <=largeur*largeur-2: #si la case est sur la dernière ligne
    if map[position_actuel-largeur-1] == "F": # en haut a gauche
      map[position_actuel-largeur-1] = "f"
    if map[position_actuel-largeur] == "F": # en haut
      map[position_actuel-largeur]  = "f"
    if map[position_actuel-largeur+1] == "F": # en haut a droite
      map[position_actuel-largeur+1] = "f"
    if map[position_actuel-1] == "F": # a gauche
      map[position_actuel-1]  = "f"
    if map[position_actuel+1] == "F": # a droite
      map[position_actuel+1]  = "f"

  elif position_actuel > largeur-1 and position_actuel < largeur*largeur-largeur: #si la case est au centre
    if map[position_actuel-largeur-1] == "F": # en haut a gauche
      map[position_actuel-largeur-1] = "f"
    if map[position_actuel-largeur] == "F": # en haut
      map[position_actuel-largeur]  = "f"
    if map[position_actuel-largeur+1] == "F": # en haut a droite
      map[position_actuel-largeur+1] = "f"
    if map[position_actuel-1] == "F": # a gauche
      map[position_actuel-1]  = "f"
    if map[position_actuel+1] == "F": # a droite
      map[position_actuel+1]  = "f"
    if map[position_actuel+largeur-1] == "F": # en bas a gauche
      map[position_actuel+largeur-1] = "f"
    if map[position_actuel+largeur] == "F": # en bas
      map[position_actuel+largeur]  = "f"
    if map[position_actuel+largeur+1] == "F": # en bas a droite
      map[position_actuel+largeur+1] = "f"

  if map[position_donjon] == "f":
    map[position_donjon] = "D"

  return map
################################################### MAP
######################################################################################################
################################################### MENU


def menu_deplacement(): # FONCTION QUAND ON DEMANDE OU ALLER
  print(Fore.RESET)
  print('#########################################')
  print('##############  DEPLACEMENT  ############')
  print('#########################################')
  print('         -     haut = 8             -    ')
  print('         - Gauche = 4   6 = Droite  -    ')
  print('         -      bas = 2             -    ')
  print('         -                          -    ')

def village (): # FONCTION QUAND ON RENTRE DANS UN VILLAGE
    check_quete_annexe()
    os.system('clear')
    print ('###################################')
    print ('### Vous entrez dans le village ###')
    print ('###################################\n')
    print ('Voici tout ce qui est possible de faire dans le village')
    print ('   -  1    Quête annêxe      -')
    print ('   -  2      Boutique        -')
    print ('   -  3  Quitter le village  -')
    village_screen_selection()

def about_menu():
    print ('#########################################')
    print ('#########       A savoir !      #########')
    print ('#########################################')
    print ('Ecrivez Haut, Bas, Gauche, Droite pour bouger')
    print ('Vous avez le choix entre 3 classes différentes pour débuter :')
    print (" Guerrier (Commence la partie avec une épée, le guerrier gagne de la furie en attaquant ses ennemies, il peut ensuite consommer cette furie pour assainer de puissants coups !")
    print (" Mage     (Commence la partie avec un baton magique, il peut consommer sa mana pour lancer des boules de feu, bien plus puissantes que ses simples projectiles de glace !")
    print (" Chasseur (Commence la partie avec un arc, il peut consommer son énergie pour lancer des coups multiples, bien plus puissants que ses simples flèches !")
    title_screen_selections()

def village_screen_selection():     # FONCTION POUR DEMANDER AU JOUEUR CE QU IL VEUT FAIRE DANS LE VILLAGE
    print("Que voulez vous faire ?")
    option = input("> ")
    while option.lower() not in ["1","2","3",]:
        print ("Veuillez insérer une commande valide.")
        option = input("> ")
    if option.lower() == "1":
        quete_annexe()
    elif option.lower() == "2":
        boutique()
    elif option.lower() == "3":
        print ("Etes-vous sûr de vouloir quitter le village? \n 1 - oui / 2 - non")
        option = input ("> ")
        while option.lower() not in ["1","2"]:
            print("Veuillez choisir entre 1 et 2")
            option = input ("> ")
        if option.lower() == "1":
            pass
        elif option.lower() == "2":
            pass

def start ():
    os.system('clear')
    print ('#########################################')
    print ('######### Bienvenue sur le RPG  #########')
    print ('#########################################')
    print ('         - 1 Create New Game -           ')
    print ('         - 2 Load Saved Game -           ')
    print ('         - 3     About       -           ')
    print ('         - 4     Exit        -           ')
    title_screen_selections()


def title_screen_selections():
    print ("Que voulez vous faire ? ")
    option = input("> ")
    while option.lower() not in ["1","2","3","4"]:
        print ("Veuillez insérer une commande valide.")
        option = input("> ")
    if option.lower() == "1":
        start_game()
    elif option.lower() == "2":
        return
    elif option.lower() == "3":
        about_menu()
    elif option.lower() == "4":
        print ("Etes-vous sûr de vouloir quitter ? \n 1 - oui / 2 - non")
        option = input ("> ")
        while option.lower() not in ["1","2"]:
            print("Veuillez choisir entre 1 et 2")
            option = input ("> ")
        if option.lower() == "1":
            sys.exit()
        elif option.lower() == "2":
            start()


################################################### MENU
######################################################################################################
################################################### AUTRE

def start_game():
    set_player_attribute()

start_weapon = {
    "épée":{"attack":10},
    "baton magique":{"attack":10},
    "arc courbé":{"attack":10}
}
################################################### AUTRE
######################################################################################################
################################################### BOUCLE PRINCIPALE
  

nb_villages = 3 # afin d'avoir un affichage minimum correct il est recommandé d'avoir au maximum un nombre de vilage a la moité de la largeur (ex : 15 villages pour 30 de largeur)
largeur = 10

map = creation_map(largeur,nb_villages)
start()

while True:
  affichage_map(map,largeur)
  # que désire faire le joueur ?
  map = deplacement_du_joueur(map,largeur)
  # fonction permettant de savoir si le joueur est dans la foret
  # SI le joueur n'est pas dans le donjon
  #     SI rentre dans la foret
  #         SI random == 2
  #             Combat commance
  #         SINON random == 1
  #             pas de combat
  #     SINON rentre dans un village
  #         que désire faire le joueur dans le village ?
  #     SINON rentre dans une safe zone
  #         il ne se passe rien le joueur peut rebouger
  #
  # SINON le joueur est dans le donjon
  #     déroulement du combat dans le donjon

  # finire shop
  # potion dans les comabats
  # dico monstres donjon
  # story telling
  # limite d'inventaire par objet 
  # fonction switch d'arme lors de l'achat de l'arme

  # systeme de decouverte de la map
  #