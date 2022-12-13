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

def creation_liste_position_dispo():
  liste = []
  for i in range(0,100):
    liste.append(i)
  return liste

def generation_de_map():
  map = []
  for i in range(100):
    map.append("-")
  
  return map

def generateur_villages():
  global premier_villages_position
  global deuxieme_villages_position
  global nb_villages


  map = generation_de_map()

  liste_position_dispo = creation_liste_position_dispo()
  

  for i in range(1,4):
    position = liste_position_dispo[random.randint(0,99)]
    
    del liste_position_dispo[position]

    map[position] = i
    if i == 1:
      premier_villages_position = position
    elif i == 2 : 
      deuxieme_villages_position = position
    else :
      troisieme_villages_position = position
  return map




def afficher_map():
  global nb_villages
  global premier_villages_position
  global deuxieme_villages_position
  i = 0
  map = generateur_villages()
  
  while i < len(map):
    if i%10 == 0:
      print()
    print(map[i],end = " ")
    i += 1

joueur_stats = mage()

nb_villages = 3
premier_villages_position   = 0
deuxieme_villages_position  = 0
troisieme_villages_position = 0

afficher_map()
