import random

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

def generation_de_map(map):
  for i in range(100):
    map.append("-")
  return map

def creation_liste_position_dispo():
  liste = []
  for i in range(0,100):
    liste.append(i)
  return liste

def generateur_villages(map,nb_villages):
  global premier_villages_position
  global deuxieme_villages_position

  liste_position_dispo = creation_liste_position_dispo()

  for i in range(1,nb_villages+1):
    position = liste_position_dispo[random.randint(0,99)]
    
    del liste_position_dispo[position]

    map[position] = i
    if i == 1:
      premier_villages_position = position
    else : 
      deuxieme_villages_position = position
  return map


def afficher_map(map):
  i = 0
  while i < len(map):
    if i%10 == 0:
      print()
    print(map[i],end = " ")
    i += 1
  print()

def connexion_villages(premiere_position,deuxieme_position,map):
  #verifie si les villages sont sur la meme collonnes 
  dernier_chifre_premiere_position = str(premiere_position)[-1]
  dernier_chifre_deuxieme_position = str(deuxieme_position)[-1]
  premier_chifre_premiere_position = str(premiere_position)[0]
  premier_chifre_deuxieme_position = str(premiere_position)[0]

  if dernier_chifre_premiere_position == dernier_chifre_deuxieme_position:
    return
  return
    

joueur_stats = mage()

carte = []
premier_villages_position = 0
deuxieme_villages_position = 0


generation_de_map(carte)

nb_villages = 2

generateur_villages(carte,nb_villages)
print(f"il y a {nb_villages} villages")
print(f"la position du premier est en {premier_villages_position} et le deuxieme {deuxieme_villages_position}")
afficher_map(carte)
