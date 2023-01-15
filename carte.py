import random
from colorama import init, Fore

###################################################
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
  while i < largeur*largeur:
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

  print(Fore.RESET+"\n")

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

def choix_de_direction(map, largeur):
  menu_deplacement()
  choix = input("Que voulez vous faire ? : ")
  while choix not in ["2","4","6","8"]:
    print("\nmerci de renseigner la bonne valeur\n")
    affichage_map(map, largeur)
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
  choix = choix_de_direction(map, largeur)

  while not verification_possibilite_deplacement(map,choix,largeur):
    print("\nHors map. merci de rester dans la map\n")
    affichage_map(map, largeur)    
    choix = choix_de_direction(map, largeur)


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
  print("+" + "-"*45 + "+")
  print("|" + " "*17 + "DEPLACEMENT" + " "*17 + "|")
  print("|" + " "*45 + "|")
  print("|" + " "*18 + " ↑ = 8" + " "*21 + "|")
  print("|" + " "*10 + " ← = 4          → = 6 " + " "*13 + "|")
  print("|" + " "*18 + " ↓ = 2" + " "*21 + "|")
  print("+" + "-"*45 + "+")


