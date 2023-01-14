import sys
import os
import time
import random
import time
from classes.Mage import Mage
from dictionaries import *
from classes.Guerrier import Guerrier
from classes.Chasseur import Chasseur
from classes.Monster import Monster
from utils import script
import colorama
from carte import *


# from village import *
#afficher les pv / pv max 
#si pas de potion, ne pas lancer la fonction
#Afficher la carte après les combats 
#trouver une fin à l'histoire
#checker pq les pv se lancent 2 fois
#quitter le village ??
# clear quand on rentre dans le donjon

#checker si les quetes fonctionnent, si l'ajout d'item à l'inventaire fonctionne, si on peut vendre les items, si le shop fonctionne,
#attribuer les armes pour chaque classe
#finir le village avec le shop - limite d'achat dans le shop, ajouter les items en string dans l'inv, à l'achat de l'arme, changer la variable current weap dans les classes
        # fonction switch d'arme lors de l'achat de l'arme



def story ():   # Scénario du début avec la possibilité de le skip lorsqu'on recommence une partie
    global player_name
    print("Voulez vous passer le scénario ?  1 - oui / 2 - non")
    player_answer = input("> ")
    while player_answer not in ["1","2"]:
        print("Veuillez répondre par 1 ou par 2")
        player_answer = input("> ")
    if player_answer == "1":
        entry = "Veuillez insérer votre nom d'aventurier : \n"
        script(entry,0.03,0)
        player_name = input("> ")
        while len(player_name) > 15 or len(player_name) < 3:
            print("Votre nom doit être compris entre 3 et 15 caractères")
            player_name = input("> ")
    elif player_answer == "2":
        os.system('cls')
        time.sleep(1)
        entry = "...\n"
        script(entry,0.5,0)
        entry = "Vous vous réveillez,"
        script(entry,0.04,0.5)
        entry = " le sol à l'air de trembler.\n"
        script(entry,0.04,1.2)
        entry = "En ouvrant les yeux,"
        script(entry,0.04,0.5)
        entry = " vous vous rendez compte que vous êtes à l'arrière d'une calèche.\n"
        script(entry,0.04,1.5)
        entry = "A l'avant se trouvent deux hommes vêtus tout deux d'une capuche,"
        script(entry,0.04,0.8)
        entry = " vous tendez l'oreille...\n"
        script(entry,0.04,1)
        entry = "Le premier homme :\n"
        script(entry,0.02,1)
        entry = "« Je crois que c'est lui,"
        script(entry,0.04,0.5)
        entry = " je le sens ... »\n"
        script(entry,0.04,1)
        entry = "- Oui j'ai le même pressentiment. \n"
        script(entry,0.04,1)
        entry = "Vous refermez les yeux, la fatigue est insoutenable.\n\n"
        script(entry,0.04,0.5)
        entry = "\x1B[3mEn fin de journée ...\n\n\x1B[23m"
        script(entry,0.02,0.5)
        entry = "Le même homme se tient devant vous.\n"
        script(entry,0.04,0.5)
        entry ="Il vous explique que vous avez fait naufrage et qu'il vous a récupéré sur la plage dans la matinée en allant pêcher."
        script(entry,0.04,1.5)
        print ("\n1 > Où suis-je ?\n2 > Qui êtes-vous ?")
        player_answer = input("> ")
        while player_answer not in ["1","2"]:
            print("Répondez par 1 ou 2")
            player_answer = input("> ")   
        if player_answer == "1":
            entry = "« Tu te trouves au village de Valdrindor,"
            script(entry,0.04,0.3)
            entry = " l'un des nombreux villages de la Forêt de Eldrida.\n"
            script(entry,0.04,0.7) 
            entry = "Comment te nommes-tu étranger ? »\n"
            script(entry,0.04,1) 
            player_name = input("> ")
            while len(player_name) > 15 or len(player_name) < 3:
                print("Votre nom doit être compris entre 3 et 15 caractères")
                player_name = input("> ")
            time.sleep(0.5)
            entry = f"{player_name} ? "
            script(entry,0.04,0.5)
            entry = "C'est peu commun !"
            script(entry,0.04,0.5)
            entry = f" Heureux de faire ta connaissance {player_name} !\n\n"
            script(entry,0.04,1)    


        elif player_answer == "2":
            entry = "« Je me nomme Nerathor,"
            script(entry,0.04,0.3)
            entry = " je suis le pêcheur du village.\n"
            script(entry,0.04,0.5)
            entry = "Comment te nommes-tu étranger ? »\n"
            script(entry,0.04,1) 
            player_name = input("> ")
            while len(player_name) > 15 or len(player_name) < 3:
                print("Votre nom doit être compris entre 3 et 15 caractères")
                player_name = input("> ")
            time.sleep(0.5)
            entry = f"{player_name} ? "
            script(entry,0.04,0.5)
            entry = "C'est peu commun !"
            script(entry,0.04,0.5)
            entry = f" Heureux de faire ta connaissance {player_name} !\n\n"
            script(entry,0.04,1)


        entry = "En faisant la connaissance de Nerathor,"
        script(entry,0.04,0.3)
        entry = " vous appenez que la moitié du village à disparu à cause d'un sorcier maléfique.\n"
        script(entry,0.04,0.5)
        entry = "Nul ne sait qui se cache derrière son identité,"
        script(entry,0.04,0.3)
        entry = " mais un but vous a été confié : \n"
        script(entry,0.04,1)
        entry = "Vous devez arrêter la propagation du mal.\n\n"
        script(entry,0.06,0.5)
        entry = "En parlant à d'autres villageois,"
        script(entry, 0.04,0.3)
        entry = " vous apprenez que le sorcier maléfique se cache dans son donjon au coeur de la forêt de Eldrida.\n"
        script(entry, 0.04,0.5)
        entry = "Les villageois vous ont mis en garde quant à la difficulté d'y pénétrer !\n"
        script(entry,0.04,1.3)

        
        print ("Nerathor :\n")
        time.sleep(1)
        entry = "« Tu vas devoir t'entraîner dur pour réussir,"
        script(entry,0.04,0.3)
        entry =" es tu prêt ? »\n"
        script(entry,0.04,0.8)
        print ("1 - Oui / 2 - Non")
        player_answer = input("> ")
        while player_answer not in ["1","2"]:
            print("Répondez par 1 ou 2")
            player_answer = input("> ")
        if player_answer == "1":
            entry = " - Oui je suis prêt à vous aider !\n"
            script(entry,0.04,0.5)
            entry = " - Très bien,"
            script(entry,0.04,0.3)
            entry = f" débutons ton entraînement {player_name}.»\n"
            script(entry,0.04,1.5)

        elif player_answer == "2":
            entry = "- Je ne pense pas être prêt à vous aider ...\n"
            script (entry,0.04,0.5)
            entry ="- Tu seras prêt en temps voulu,"
            script(entry,0.04,0.3)
            entry = f" ne t'en fais pas {player_name}.\n"
            script(entry,0.04,1.5)


        entry = "\x1B[3m6 mois plus tard ...\n\x1B[23m"
        script(entry,0.02,2.5)





def boucle():

    print("Vous voilà au village de Valdrindor")
    print ("Votre personnage se trouve sur le point jaune fluo")
    print ("Voici une visualisation de la carte de haut : ")
    global game
    largeur = 10
    nb_village = 2
    map = creation_map(largeur,nb_village)                                   #la map est basé sur un 10 x 10 avec 3 villages et un donjon, possibilité de modifier ces valeurs
    affichage_map(map,largeur)
    satisfied = False 
    while satisfied == False:
        print ("Voulez vous générer une nouvelle carte ?\n 1 - oui / 2 - non")
        player_choice = input("> ")
        while player_choice not in ["1","2"]:
            print ("Veuillez répondre par 1 ou par 2")
            player_choice = input("> ")
        if player_choice == "1":
            os.system('cls')
            map = creation_map(largeur,nb_village)
            affichage_map(map,largeur)

        elif player_choice =="2":
            satisfied = True
            os.system("cls")

    affichage_map(map,largeur)
    game = True
    while game == True:
        
        # que désire faire le joueur ?
        map = deplacement_du_joueur(map,largeur)
        affichage_map(map,largeur)
        if map[map[-1]] == "f":     # map[-1] = la case dans laquelle le joueur se trouve 
            is_monster = random.randint(0,1)
            if is_monster < 0.5:
                start_combat()
        elif map[-1] == map[-2]:                  # map[-2] = la case dans laquelle se trouve le donjon
            entry = "Etes-vous sur de vouloir rentrer dans le donjon ?\n"
            script (entry,0.05,1)
            print("1 - Oui / 2 - Non")
            player_choice = input("> ")
            while player_choice not in ["1","2"]:
                print("Veuillez répondre par 1 ou par 2")
                player_choice = input("> ")
            if player_choice == "1":
                dungeon_scenario()
            elif player_choice == "2":
                pass
        elif isinstance(map[map[-1]],int):
            village()

        



def dungeon_scenario ():        # Scénario de fin, toute la partie du donjon se déroule ici
    entry = "...\n"
    script(entry,0.5,0)
    entry = "Vous entrez dans le donjon\n"
    script(entry,0.03,0.5)
    entry = "Un gnome tapi dans l'ombre s'approche ...\n"
    script(entry,0.03,0.5)
    entry = "« Tu n'aurais jamais du venir ici !"
    script(entry, 0.05,0.3)
    entry = " Il t'est désormais impossible de rebrousser chemin ! »\n"
    script(entry,0.05,0)
    entry = "\x1B[3mLa porte du donjon se referme derrière vous !\n\x1B[23m"
    script(entry,0.01,1.5)
    print ("Réponse : \n1 > L'interroger sur la prophétie\n2 > Le tuer")
    player_answer = input("> ")
    while player_answer not in ["1","2"]:
        print("Répondez par 1 ou 2")
        player_answer = input("> ")
    if player_answer == "1":
        entry = "« Que sais tu sur la prophétie ? »\n"
        script(entry,0.04,1)
        entry ="- La prophétie du Python ?"
        script(entry,0.05,0.3)
        entry =" Tu en sauras bien assez tôt ...\n"
        script(entry,0.05,1)
        entry = "- Parle moi du magicien noir ou je te tue !\n"
        script(entry,0.04,0.5)
        entry = "- Je ne trahirai pas mon maître !"
        script(entry,0.05,0.3)
        entry = " Bientôt, les ténèbres s'abbatront sur cette terre !\n"
        script(entry,0.05,0)
        entry = "\x1B[3mLe gobelin brandit la dague posée sur la table\n\x1B[23m"
        script(entry,0.01,2)
        player_choice = input("Insérez n'importe quelle touche pour débuter le combat : ")
        os.system('cls')
        gnome = boss_monsters["gnome"]
        boss_monster = Monster(gnome, gnome['health'],gnome["attack"],gnome["speed"],gnome["xp"],gnome["loots"])
        if isinstance(player,Mage):
            start_mage_combat(boss_monster)
        elif isinstance(player,Chasseur):
            start_chasseur_combat(boss_monster)
        elif isinstance(player,Guerrier):
            start_guerrier_combat(boss_monster)



def start ():
    print ('#########################################')
    print ('######### Bienvenue sur le RPG  #########')
    print ('#########################################')
    print ('         - 1 Create New Game -           ')
    print ('         - 2     About       -           ')
    print ('         - 3     Exit        -           ')
    title_screen_selections()


def title_screen_selections():
    print ("Que voulez vous faire ? ")
    option = input("> ")
    while option.lower() not in ["1","2","3"]:
        print ("Veuillez insérer une commande valide.")
        option = input("> ")
    if option.lower() == "1":
        start_game()
    elif option.lower() == "2":
        about_menu()
    elif option.lower() == "3":
        print ("Etes-vous sûr de vouloir quitter ? \n 1 - oui / 2 - non")
        option = input ("> ")
        while option.lower() not in ["1","2"]:
            print("Veuillez choisir entre 1 et 2")
            option = input ("> ")
        if option.lower() == "1":
            sys.exit()
        elif option.lower() == "2":
            start()

def set_player_attribute():
    global player_gender
    global player
    
    
    
    entry = "Renseignez le sexe de votre personnage : H - F \n"
    script(entry,0.03,0.3)
    
    player_gender = input("> ")
    while player_gender.lower() not in ["h","f"]:
        print ("Veuillez répondre par H ou F")
        player_gender = input("> ")

    entry = "Il est désormais temps pour vous de choisir une classe : \n"
    script(entry,0.03,0.3)
    print("~~~~~~ Choix de la classe ~~~~~~ \n  1 - Guerrier   2 - Mage   3 - Chasseur \n")

    player = input("> ")
    while player.lower() not in ["1","2","3"]:
        print("Veuillez sélectionner une classe")
        player = input("> ")
    if player.lower() == "1":
        player = Guerrier()
        if player_gender.lower() == "h":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " le guerrier aux milles épées !\n"
            script(entry,0.04,2)
        elif player_gender.lower() == "f":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " la guerrière aux milles épées !\n"
            script(entry,0.04,2)
            




    elif player.lower() == "2":
        player = Mage()
        if player_gender.lower() == "h":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " le mage aux boules de feu étincelantes !\n"
            script(entry,0.04,2)
        elif player_gender.lower() == "f":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " la mage aux boules de feu étincelantes !\n"
            script(entry,0.04,2)

    elif player.lower() == "3":
        player = Chasseur()
        if player_gender.lower() == "h":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " le chasseur au flair aiguisé"
            script(entry,0.04,2)
        elif player_gender.lower() == "f":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " la chasseuse au flair aiguisé"
            script(entry,0.04,2)
    
    os.system("cls")


def start_game():
    story()
    set_player_attribute()

    boucle()

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
    
def check_potion():
    if "potion de soin mineure" and "potion de soin supérieure" and "potion de force mineure" and "potion de soin supérireure" and "potion de mana mineure" and "potion de mana supérireure" and "potion d'énergie mineure" and "potion d'énergie supérieure" not in player.inventory:
        pass
    print("Voulez vous : 1 - Utiliser une potion / 2 - Combattre")
    player_choice = input("> ")
    while player_choice not in ["1","2"]:
        print("Veuillez choisir entre 1 - utiliser une potion ou 2 - combattre")
        player_choice = input("> ")
    if player_choice == "2":
        return
    elif player_choice == "1":
        
        print ("Voulez vous :\n1) Utiliser une potion de soin\n2) Utiliser une potion de mana / énergie\n3) Utiliser une potion de force")
        player_choice = input ("> ")
        while player_choice.lower() not in ["1","2","3",]:
            print ("Veuillez choisir entre 1 - utiliser une potion de soin 2 - utiliser une potion de mana / énergie ou 3 - utiliser une potion de force")
            player_choice = input ("> ")
        if player_choice == "1":
            if "potion de soin mineure" not in player.inventory and "potion de soin supérieure" not in player.inventory:
                print ("Vous n'avez pas de potion de soin")
                check_potion()
            elif "potion de soin mineure" in player.inventory and "potion de soin supérieure" in player.inventory:
                print ("Voulez vous utiliser une potion de soin : 1 - mineure / 2 - supérieure")
                health_pot_check = input("> ")
                while health_pot_check not in ["1","2"]:
                    print ("Veuillez sélectionner une potion entre 1 et 2 ")
                    health_pot_check = input ("> ")
                if health_pot_check == "1":
                        player.inventory.remove("potion de soin mineure")
                        player.health += 150
                        if player.health > player.max_health:
                            player.health = player.max_health
                elif health_pot_check == "2":
                    player.inventory.remove("potion de soin supérieure")
                    player.health += 300
                    if player.health > player.max_health:
                        player.health = player.max_health
            elif "potion de soin mineure" in player.inventory and "potion de soin supérieure" not in player.inventory:
                print ("Vous ne possédez pas de potion de soin supérieure\nUtilisation d'une potion de soin mineure")
                player.inventory.remove("potion de soin mineure")
                player.health += 150
                if player.health > player.max_health:
                    player.health = player.max_health
            elif "potion de soin mineure" not in player.inventory and "potion de soin supérieure" in player.inventory:
                print ("Vous ne possédez pas de potion de soin mineure\nUtilisation d'une potion de soin supérieure")
                player.inventory.remove("potion de soin supérieure")
                player.health += 300
                if player.health > player.max_health:
                    player.health = player.max_health
                    
                    
        elif player_choice == "2":
            if isinstance(player,Guerrier):
                print("Vous ne pouvez pas utiliser de potion de mana / énergie")
                check_potion()
            if isinstance(player,Mage):
                if "potion de mana mineure" not in player.inventory and "potion de mana supérieure" not in player.inventory:
                    print ("Vous n'avez pas de potion de mana")
                    check_potion()
                elif "potion de mana mineure" in player.inventory and "potion de mana supérieure" in player.inventory:
                    print ("Voulez vous utiliser une potion de mana : 1 - mineure / 2 - supérieure")
                    health_pot_check = input("> ")
                    while health_pot_check not in ["1","2"]:
                        print ("Veuillez sélectionner une potion entre 1 et 2 ")
                        health_pot_check = input ("> ")
                    if health_pot_check == "1":
                            player.inventory.remove("potion de mana mineure")
                            player.mana += 30
                            if player.mana >player.max_mana:
                                player.mana =player.max_mana
                    elif health_pot_check == "2":
                        player.inventory.remove("potion de mana supérieure")
                        player.mana += 50
                        if player.mana >player.max_mana:
                            player.mana =player.max_mana
                elif "potion de mana mineure" in player.inventory and "potion de mana supérieure" not in player.inventory:
                    print ("Vous ne possédez pas de potion de mana supérieure\nUtilisation d'une potion de mana mineure")
                    player.inventory.remove("potion de mana mineure")
                    player.mana += 30
                    if player.mana >player.max_mana:
                        player.mana =player.max_mana
                elif "potion de mana mineure" not in player.inventory and "potion de mana supérieure" in player.inventory:
                    print ("Vous ne possédez pas de potion de mana mineure\nUtilisation d'une potion de mana supérieure")
                    player.inventory.remove("potion de mana supérieure")
                    player.mana += 50
                    if player.mana >player.max_mana:
                        player.mana =player.max_mana
                        
            elif isinstance(player,Chasseur):
                if "potion d'énergie mineure" not in player.inventory and "potion d'énergie supérieure" not in player.inventory:
                    print ("Vous n'avez pas de potion d'énergie")
                    check_potion()
                elif "potion d'énergie mineure" in player.inventory and "potion d'énergie supérieure" in player.inventory:
                    print ("Voulez vous utiliser une potion d'énergie : 1 - mineure / 2 - supérieure")
                    health_pot_check = input("> ")
                    while health_pot_check not in ["1","2"]:
                        print ("Veuillez sélectionner une potion entre 1 et 2 ")
                        health_pot_check = input ("> ")
                    if health_pot_check == "1":
                            player.inventory.remove("potion d'énergie mineure")
                            player.energy += 30
                            if player.energy >player.max_energy:
                                player.energy =player.max_energy
                    elif health_pot_check == "2":
                        player.inventory.remove("potion d'énergie supérieure")
                        player.energy += 50
                        if player.energy >player.max_energy:
                            player.energy =player.max_energy
                elif "potion d'énergie mineure" in player.inventory and "potion d'énergie supérieure" not in player.inventory:
                    print ("Vous ne possédez pas de potion d'énergie supérieure\nUtilisation d'une potion d'énergie mineure")
                    player.inventory.remove("potion d'énergie mineure")
                    player.energy += 30
                    if player.energy >player.max_energy:
                        player.energy =player.max_energy
                elif "potion d'énergie mineure" not in player.inventory and "potion d'énergie supérieure" in player.inventory:
                    print ("Vous ne possédez pas de potion d'énergie mineure\nUtilisation d'une potion d'énergie supérieure")
                    player.inventory.remove("potion d'énergie supérieure")
                    player.energy += 50
                    if player.energy >player.max_energy:
                        player.energy =player.max_energy
                        
                        
        elif player_choice == "3":
            if "potion de force mineure" not in player.inventory and "potion de force supérieure" not in player.inventory:
                print ("Vous n'avez pas de potion de force")
                check_potion()
        
            elif "potion de force mineure" in player.inventory and "potion de force supérieure" in player.inventory:
                print ("Voulez vous utiliser une potion de force : 1 - mineure / 2 - supérieure")
                health_pot_check = input("> ")
                while health_pot_check not in ["1","2"]:
                    print ("Veuillez sélectionner une potion entre 1 et 2 ")
                    health_pot_check = input ("> ")
                if health_pot_check == "1":
                        player.inventory.remove("potion de force mineure")
                        player.attack += 10
                        if player.health > player.max_health:
                            player.health = player.max_health
                elif health_pot_check == "2":
                    player.inventory.remove("potion de force supérieure")
                    player.attack += 30
                    if player.health > player.max_health:
                        player.health = player.max_health
            elif "potion de force mineure" in player.inventory and "potion de force supérieure" not in player.inventory:
                print ("Vous ne possédez pas de potion de force supérieure\nUtilisation d'une potion de force mineure")
                player.inventory.remove("potion de force mineure")
                player.attack += 10
                if player.health > player.max_health:
                    player.health = player.max_health
            elif "potion de force mineure" not in player.inventory and "potion de force supérieure" in player.inventory:
                print ("Vous ne possédez pas de potion de force mineure\nUtilisation d'une potion de force supérieure")
                player.inventory.remove("potion de force supérieure")
                player.attack += 30
                if player.health > player.max_health:
                    player.health = player.max_health
                     

def loot(monster):
        loot = random.randint(0,100)
        if loot >= 25:
            player_loot = random.choice(list(monster.loot))
            print (f"Vous fouillez le cadavre et vous trouvez : {player_loot} \nL'objet a été ajouté à votre inventaire...")
            player.inventory.append(player_loot)
        else:
            print("Vous ne trouvez rien sur le cadavre")

def start_combat():

    monster = Monster()
    
    player.attack = player.max_attack
    print (f"Un ennemi approche ! C'est un(e) {monster.type}")
    print ("Souhaitez vous : 1 - combattre / 2 - fuir ?")
    player_choice = input("> ")
    while player_choice.lower() not in ["1","2"]:
        print("Veuillez taper 1 pour combattre, 2 pour fuir")
        player_choice = input("> ")
    if player_choice.lower() == "2":
        escape = random.randint(0,100)
        if escape < player.luck:
            print ("Succès ! Vous fuyez le combat")
        else:
            print ("Échec ! Vous devez combattre !")
            if isinstance(player,Mage):
                start_mage_combat(monster)
                
            elif isinstance(player,Chasseur):
                start_chasseur_combat(monster)
                
            elif isinstance(player,Guerrier):
                start_guerrier_combat(monster)
                        
    elif player_choice.lower() == "1":
        if isinstance(player,Mage):
            start_mage_combat(monster)
            
        elif isinstance(player,Chasseur):
            start_chasseur_combat(monster)
            
        elif isinstance(player,Guerrier):
            start_guerrier_combat(monster) 

def start_guerrier_combat(monster):
    global game
    player.fury = 0
    
    print ("-------------------------------------------")
    print (f"VOS HP : {player.health}     |    HP DE L'ENNEMI : {monster.health}")
    print ("-------------------------------------------")
    
    
    if player.speed <= monster.speed:
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("L'ennemi(e) attaque en premier !")
        player.health -= monster.attack
        print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over \n!"
            script(entry,0.07,0)
            game = False
            start()
    else:
        print (f"Il vous reste {player.health} HP")
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("Vous attaquez en premier !")
    

    while player.health > 0 or monster.health > 0:
        check_potion()
        if player.fury > 100:
            player.fury = 100
        if player.fury >= 30:
            print (f"Votre furie est de {player.fury}, souhaitez-vous assainer un puissant coup ? \n1 - oui / 2 - non ?")
            check_fury = input("> ")
            while check_fury not in ["1","2"]:
                print("Veuillez répondre par 1 ou par 2")
                check_fury = input("> ")
            if check_fury == "1":
                player.fury -= 30
                print("Chaaarge !!!")
                
                player_attack = player.attack + player.strenght
                monster.health -= player_attack
                if monster.health <= 0:
                    print (f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                    print ("Vous triomphez ! Votre ennemi(e) est mort !")
                    break
                else:
                    print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')
                
                player.health -= monster.attack
                print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
                        
                if player.health <= 0:
                    entry = "Vous succombez de vos blessures !!! \nGame over \n!"
                    script(entry,0.07,0)
                    game = False
                    start()
                    
                else :
                    print(f"Il vous reste {player.health} HP")

            elif check_fury == "2":
                print ("Souhaitez vous donner un coup d'épée ou effectuer une évocation ?")
                print ("1 - coup d'épée / 2 - évocation ")
                player_choice = input("> ")
                while player_choice not in ["1","2"]:
                    print ("Veuillez choisir 1 ou 2")
                    player_choice = input("> ")
                if player_choice == "1":
                    print ("Coup d'épée !")
                    player_attack = player.attack
                    monster.health -= player_attack
                    
                    if monster.health <= 0:
                        print(f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                        print ("Vous triomphez ! Votre ennemi(e) est mort !")
                        break
                    else:
                        print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')
                        player.fury += 20

                        player.health -= monster.attack
                        print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
                        
                    if player.health <= 0:
                        entry = "Vous succombez de vos blessures !!! \nGame over \n!"
                        script(entry,0.07,0)
                        game = False
                        start()
                    else :
                        print (f" Il vous reste {player.health} HP")

                elif player_choice == "2":

                    player.fury += 40
                    if player.fury > 100:
                        player.fury = 100
                    print (f'Évocation ! Votre furie est désormais de {player.fury}')
                    
                    player.health -= monster.attack
                    print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
                    if player.health <= 0:
                        entry = "Vous succombez de vos blessures !!! \nGame over \n!"
                        script(entry,0.07,0)
                        game = False
                        start()
                    else :
                         print(f"Il vous reste {player.health} HP")
                        

        else:
            print (f"Votre furie est de {player.fury}, vous n'avez pas assez pour lancer un puissant coup !")
            print ("Souhaitez vous donner un coup d'épée ou effectuer une évocation ?")
            print ("1 - coup d'épée / 2 - évocation ")
            player_choice = input("> ")
            while player_choice not in ["1","2"]:
                print ("Veuillez choisir 1 ou 2")
                player_choice = input("> ")
            if player_choice == "1":
                print ("Coup d'épée !")
                player_attack = player.attack
                monster.health -= player_attack
                player.fury += 20
                
                if monster.health <= 0:
                    print(f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                    print ("Vous triomphez ! Votre ennemi(e) est mort !")
                    break
                else:
                    print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')


                
                player.health -= monster.attack
                print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
                
                if player.health <= 0:
                    entry = "Vous succombez de vos blessures !!! \nGame over \n!"
                    script(entry,0.07,0)
                    start()
                else :
                    print(f" Il vous reste {player.health} HP")
                    
            elif player_choice == "2":

                player.fury += 40
                if player.fury > 100:
                    player.fury = 100
                print (f'Évocation ! Votre furie est désormais de {player.fury}')
                
                player.health -= monster.attack
                print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
                
                if player.health <= 0:
                    entry = "Vous succombez de vos blessures !!! \nGame over \n!"
                    script(entry,0.07,0)
                    start()
                else :
                    print (f" Il vous reste {player.health} HP")
    if monster.health <= 0:
        
        
        if player.level == 20:
            pass
        else:
            player.xp += monster.xp
            print (f"Vous obtenez {monster.xp} points d'expériences ! ")
            if player.xp >= player.xp_to_lvl_up:
                player.level_up()
            
            print (f"Vous êtes à {player.xp} / {player.xp_to_lvl_up} points d'expérience pour le prochain niveau.")
                
                
    if monster.health <= 0 and monster.is_random:
        loot(monster)
    
    

            
def start_chasseur_combat(monster):
    

    print ("-------------------------------------------")
    print (f"VOS HP : {player.health}     |    HP DE L'ENNEMI : {monster.health}")
    print ("-------------------------------------------")
    
    if player.speed <= monster.speed:
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("L'ennemi(e) attaque en premier !")
        player.health -= monster.attack
        print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over \n!"
            script(entry,0.07,0)
            game = False
            start()
    else:
        print (f"Il vous reste {player.health} HP")
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("Vous attaquez en premier !")

    while player.health > 0 or monster.health > 0:
        check_potion()
        if player.energy > 100:
            player.energy = 100
        if player.energy >= 20:
            print (f"Votre énergie est de {player.energy}, souhaitez-vous lancer Flèches multiples ? \n1 - oui / 2 - non ?")
            check_energy = input("> ")
            while check_energy not in ["1","2"]:
                print("Veuillez répondre par 1 ou par 2")
                check_energy = input("> ")
            if check_energy == "1":
                player.energy -= 20
                print("Flèches multiples !!!")
                player_attack = player.attack + player.agility
                monster.health -= player_attack

            elif check_energy == "2":
                print ("Tir de flèche !")
                player_attack = player.attack
                monster.health -= player_attack
                player.energy += 5
                
            if monster.health <= 0:
                print(f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                break
            else :
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')
                    
            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
            if player.health <= 0:
                entry = "Vous succombez de vos blessures !!! \nGame over \n!"
                script(entry,0.07,0)
                start()
            else:
                print (f"Il vous reste {player.health} HP")
        else:
            print (f"Votre énergie est de {player.energy}, vous n'avez pas assez pour lancer vos flèches multiples !")
            print ("Tir de flèche !")
            player_attack = player.attack
            monster.health -= player_attack
            player.energy += 5
            if monster.health <= 0:
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                print(f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                break
            else :
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')

            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
            
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over \n!"
            script(entry,0.07,0)
            start()
        else:
            print(f" Il vous reste {player.health} HP")
    if monster.health <= 0:
        if player.level == 20:
            pass
        else:
            player.xp += monster.xp
            print (f"Vous obtenez {monster.xp} points d'expériences ! ")
            if player.xp >= player.xp_to_lvl_up:
                player.level_up()
            
            print (f"Vous êtes à {player.xp} / {player.xp_to_lvl_up} points d'expérience pour le prochain niveau.")
                
    if monster.health <= 0 and monster.is_random:
        loot(monster)
        

    



def start_mage_combat(monster):
    
    
    print ("-------------------------------------------")
    print (f"VOS HP : {player.health}     |    HP DE L'ENNEMI : {monster.health}")
    print ("-------------------------------------------")


    if player.speed <= monster.speed:
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("L'ennemi(e) attaque en premier !")
        player.health -= monster.attack
        print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over \n!"
            script(entry,0.07,0)
            game = False
            start()
    else:
        print (f"Il vous reste {player.health} HP")
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("Vous attaquez en premier !")
    
    while player.health > 0 or monster.health > 0:
        check_potion()
        if player.mana > 100:
            player.mana = 100
        if player.mana >= 20:
            print (f"Votre mana est de {player.mana}, souhaitez-vous lancer une boule de feu ? \n1 - oui / 2 - non ?")
            check_mana = input("> ")
            while check_mana not in ["1","2"]:
                print("Veuillez répondre par 1 ou par 2")
                check_mana = input("> ")
            if check_mana == "1":
                player.mana -= 20
                print("Bouuuule de feu !!!")
                player_attack = player.attack + player.intelligence
                monster.health -= player_attack

            elif check_mana == "2":
                print ("Projectile de glace !")
                player_attack = player.attack
                monster.health -= player_attack
                player.mana += 10
            if monster.health <= 0:
                    print ("Vous triomphez ! Votre ennemi(e) est mort !")
                    print(f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                    break
            else:
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')
                player.mana
                    
            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
            if player.health <= 0:
                entry = "Vous succombez de vos blessures !!! \nGame over \n!"
                script(entry,0.07,0)
                start()
            else:
                print(f"Il vous reste {player.health} HP")
        else:
            print (f"Votre mana est de {player.mana}, vous n'avez pas assez pour lancer une boule de feu !")
            print ("Projectile de glace !")
            player_attack = player.attack
            monster.health -= player_attack
            player.mana += 10
            if monster.health <= 0:
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                print(f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                break

            else:
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')
                player.mana

            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
            
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over !\n"
            script(entry,0.07,0)
            start()
        else:
            print(f"Il vous reste {player.health} HP")

    if monster.health <= 0:
        
        if player.level == 20:
            pass
        else:
            player.xp += monster.xp
            print (f"Vous obtenez {monster.xp} points d'expériences ! ")
            if player.xp >= player.xp_to_lvl_up:
                player.level_up()
            
            print (f"Vous êtes à {player.xp} / {player.xp_to_lvl_up} points d'expérience pour le prochain niveau.")
                
    if monster.health <= 0 and monster.is_random:
        loot(monster)           





def village (): # FONCTION QUAND ON RENTRE DANS UN VILLAGE
    # check_quete_annexe()
    
    print ('####################################\n')
    print ('   -  1    Quête annêxe      -   ')
    print ('   -  2      Boutique        -   ')
    print ('   -  3       Repos          -   ')
    print ('   -  4  Quitter le village  -   ')
    village_screen_selection()



def village_screen_selection():     # FONCTION POUR DEMANDER AU JOUEUR CE QU IL VEUT FAIRE DANS LE VILLAGE
    print("Que voulez vous faire ?")
    option = input("> ")
    while option.lower() not in ["1","2","3","4"]:
        print ("Veuillez insérer une commande valide.")
        option = input("> ")
    if option.lower() == "1":
        pass
    elif option.lower() == "2":
        show_boutique()
    elif option.lower() == "3":

        if player.health < player.max_health:
            player.health = player.max_health
            print ("Vous voilà reposé ... Vous récupérez vos ressources !")
        else :
            print("Vous n'avez pas besoin de vous reposer !")
        
        if isinstance (player,Mage):
            player.mana = player.max_mana
        elif isinstance (player,Chasseur):
            player.energy = player.max_energy
        village()
        
    elif option.lower() == "4":
        print ("Etes-vous sûr de vouloir quitter le village? \n 1 - oui / 2 - non")
        option = input ("> ")
        while option.lower() not in ["1","2"]:
            print("Veuillez choisir entre 1 et 2")
            option = input ("> ")
        if option.lower() == "1":
            os.system('cls')
            time.sleep(1.5)
            pass
        elif option.lower() == "2":
            village()





def show_boutique():
    print("Objets disponibles dans la boutique:")
    for item_name, item_info in items.items():
        print(f"- {item_info['name']} : {item_info['price']} gold(s) - Stock : {item_info['stock']} ")


show_boutique()























































