import random
from colorama import init, Fore


class mage:
  def __init__(self):
    self.pv = 50
    self.pm = 150
    self.xp = 0
    self.inv ={
        "arme_actuel" : "",
        "armes_stock" : "",
        "potion" : 0,
    }

class guerrier:
  def __init__(self):
    self.pv = 150
    self.pm = 50
    self.xp = 0
    self.inv ={
        "arme_actuel" : "",
        "armes_stock" : "",
        "potion" : 0,
    }

class arche:
  def __init__(self):
    self.pv = 100
    self.pm = 100
    self.xp = 0
    self.inv ={
        "arme_actuel" : "",
        "armes_stock" : "",
        "potion" : 0,
    }

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
      if map[i+1] not in liste_des_nom_village: #si la case a droite est vide
        if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
          if map[i+largeur+1] not in liste_des_nom_village: #si la case en desous a droite est vide
            map[i] = "f"

    elif i == largeur-1: #si c'est la case en haut a droite
      if map[i-1] not in liste_des_nom_village: #si la case est gauche est vide
        if map[i+largeur-1] not in liste_des_nom_village: #si la case en bas a gauche est vide
          if map[i+largeur] not in liste_des_nom_village: #si la case en desous est vide
            map[i] = "f"

    elif i == largeur*largeur-largeur : #si c'est la case en bas a gauche
      if map[i-largeur] not in liste_des_nom_village: #si la case est en haut
        if map[i-largeur-1] not in liste_des_nom_village: #si la case est en haut a droite
          if map[i+1] not in liste_des_nom_village: #si la case a droite est vide
            map[i] = "f"
  
    
    elif i == largeur*largeur-1: #si c'est la cas you en bas a droite
      if map[i-largeur] not in liste_des_nom_village: #si la case est en haut
        if map[i-largeur-1] not in liste_des_nom_village: #si la case est en haut a gauche
          if map[i-1] not in liste_des_nom_village: #si la case est gauche est vide
            map[i] = "f"

    elif i%largeur == 0 : #si la case est sur la colonne a gauche
      if map[i-largeur] not in liste_des_nom_village: #si la case est en haut
        if map[i-largeur+1] not in liste_des_nom_village: #si la case est en haut a droite
          if map[i+1] not in liste_des_nom_village: #si la case a droite est vide
            if map[i+largeur+1] not in liste_des_nom_village: #si la case en desous a droite est vide
              if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
                map[i] = "f"

    elif i in dernien_chiffre_de_la_ligne(largeur): #si la case est tout a droite
      if map[i-largeur] not in liste_des_nom_village: #si la case est en haut
        if map[i-largeur-1] not in liste_des_nom_village: #si la case est en haut a gauche
          if map[i-1] not in liste_des_nom_village: #si la case est gauche est vide
            if map[i+largeur-1] not in liste_des_nom_village: #si la case en bas a gauche est vide
              if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
                map[i] = "f"

    elif i>0 and i<largeur : #si la case est juste sur la premiere ligne
      if map[i-1] not in liste_des_nom_village: #si la case est gauche est vide
        if map[i+1] not in liste_des_nom_village: #si la case a droite est vide
          if map[i+largeur-1] not in liste_des_nom_village: #si la case en bas a gauche est vide
            if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
              if map[i+largeur+1] not in liste_des_nom_village: #si la case en desous a droite est vide
                map[i] = "f"

    elif i >= largeur*largeur-largeur-1 and i <=largeur*largeur-2: #si la case est sur la derniere ligne
      if map[i-largeur+1] not in liste_des_nom_village: #si la case est en haut a gauche
        if map[i-largeur] not in liste_des_nom_village: #si la case est en haut
          if map[i-largeur-1] not in liste_des_nom_village: #si la case est en haut a droite
            if map[i-1] not in liste_des_nom_village: #si la case est gauche est vide
              if map[i+1] not in liste_des_nom_village: #si la case a droite est vide
                map[i] = "f"

    elif i > largeur-1 and i < largeur*largeur-largeur: #si la case est au cntre
      if map[i-largeur+1] not in liste_des_nom_village: #si la case est en haut a gauche
        if map[i-largeur] not in liste_des_nom_village: #si la case est en haut
          if map[i-largeur-1] not in liste_des_nom_village: #si la case est en haut a droite
            if map[i-1] not in liste_des_nom_village: #si la case est gauche est vide
              if map[i+1] not in liste_des_nom_village: #si la case a droite est vide
                if map[i+largeur-1] not in liste_des_nom_village: #si la case en bas a gauche est vide
                  if map[i+largeur] not in liste_des_nom_village: #si la case en dessous est vide
                    if map[i+largeur+1] not in liste_des_nom_village: #si la case en desous a droite est vide
                      map[i] = "f"
    i = i + 1
  return map

def creation_map(largeur,nb_villages):
  map = 0
  map = ajout_foret_map(generateur_villages(largeur,nb_villages),nb_villages,largeur)
  
  return map

def affichage_map(map,largeur,nb_villages):
  i = 0
  couleurs = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN]
  while i < largeur*largeur:
    couleur = random.choice(couleurs)
    if i%largeur == 0:
      print()
    if isinstance(map[i], int):
      if map[i] < 10:
        print(couleur +str(map[i]),end = " ")
      else:
        print(couleur +str(map[i]),end = "")
    elif  map[i] == "-" or map[i] == "f":
      print(Fore.RESET + str(map[i]),end = " ")
    i += 1

joueur_stats = mage()

nb_villages = 10 # afin d'avoir un affichage minimum correct il est recommandé d'avoir au maximum un nombre de vilage a la moité de la largeur (ex : 15 villages pour 30 de largeur)
largeur = 20
liste_nb_village = []


map = creation_map(largeur,nb_villages)
affichage_map(map,largeur,nb_villages)