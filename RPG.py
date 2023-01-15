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
from verif_name import *





def story ():   # Scénario du début avec la possibilité de le skip lorsqu'on recommence une partie
    global player_name
    print("Voulez vous passer le scénario ?  1 - oui / 2 - non")
    player_answer = input("> ")
    while player_answer not in ["1","2"]:
        print("Veuillez répondre par 1 ou par 2")
        player_answer = input("> ")
    if player_answer == "1":
        entry = "Veuillez insérer votre nom d'aventurier : \n"     #nom du joueur si on skip le scénar 
        script(entry,0.03,0)
        player_name = input("> ")
        player_name = verif_pseudo(player_name)
    elif player_answer == "2":         #début scénario ici
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
            player_name = verif_pseudo(player_name)
            
            time.sleep(0.5)
            entry = f"{player_name} ? "
            script(entry,0.04,0.5)
            entry = "C'est peu commun !"
            script(entry,0.04,0.5)
            entry = f" Heureux de faire ta connaissance {player_name} !\n\n"
            script(entry,0.04,1)    


        elif player_answer == "2":
            entry = "«- Je me nomme Nerathor,"
            script(entry,0.04,0.3)
            entry = " je suis le pêcheur du village.\n"
            script(entry,0.04,0.5)
            entry = "Comment te nommes-tu étranger ? »\n"
            script(entry,0.04,1) 
            player_name = input("> ")
            player_name = verif_pseudo(player_name)
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




def dungeon_scenario ():        # Scénario de fin, toute la partie du donjon se déroule ici
    global game
    entry = "...\n"
    script(entry,0.5,0)
    entry = "Vous entrez dans le donjon.\n"
    script(entry,0.03,0.5)
    entry = "Un gnome tapi dans l'ombre s'approche ...\n"
    script(entry,0.03,1)
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
        entry = "- Parle moi du mage noir ou je te tue !\n"
        script(entry,0.04,1)
        entry = "- Je ne trahirai pas mon maître !"
        script(entry,0.05,0.3)
        entry = " Bientôt, les ténèbres s'abbatront sur cette terre !\n"
        script(entry,0.05,0)
        entry = "\x1B[3mLe gobelin brandit la dague posée sur la table\n\x1B[23m"
        script(entry,0.01,2)

    
    player_choice = input("Appuyez sur n'importe quelle touche pour débuter le combat : ")           #combat du gnome 
    os.system('cls')
    gnome = boss_monsters["gnome"]
    boss_monster = Monster(gnome, gnome['health'],gnome["attack"],gnome["speed"],gnome["xp"],gnome["loots"])
    if isinstance(player,Mage):
        start_mage_combat(boss_monster)
    elif isinstance(player,Chasseur):
        start_chasseur_combat(boss_monster)
    elif isinstance(player,Guerrier):
        start_guerrier_combat(boss_monster)

    time.sleep(3)
    entry = "« Bon débaras ...\n"
    script(entry,0.04,0.3)
    entry ="Ce gnome n'allait rien me dire que je veuille entendre. »\n"
    script(entry,0.04,0.1)
    entry = "\x1B[3mGROAAAAAAARRRR\n\x1B[23m"
    script(entry,0.02,1.5)
    entry ="Vous entendez l'écho d'un rugissement au loin.\n"
    script(entry,0.04,0.7)
    entry = "Vous brandissez une torche qui reposait sur une applique murale et vous décidez d'avancer...\n"
    script(entry,0.04,1)
    entry = "En avançant vous voyez que vous avez le choix entre une porte sur votre gauche et un escalier montant sur votre droite."
    script(entry,0.04,1)
    entry = "\nQue décidez vous de faire ?\n"
    script(entry,0.04,0.8)
    entry= (" 1 - Ouvrir la porte sur votre gauche 2 - Monter les escaliers à votre droite.\n")
    script(entry,0.04,1)
    player_choice = input("> ")
    while player_choice not in ["1","2"]:
        print("Veuillez répondre par 1 ou par 2")
        player_choice = input("> ")
    if player_choice == "1":
        os.system('cls')
        time.sleep(1)
        entry = "C'est un piège ! "
        script(entry,0.02,0.6)
        entry = " En ouvrant la porte vous recevez une salve de flèche !\n"
        script(entry,0.03,0.5)
        entry = "Heureusement pour vous,"
        script(entry,0.04,0.5)
        entry = " votre armure a absorbé une partie des dégâts...\n"
        script(entry,0.04,0.5)
        player.health -= 150
        entry = "Vous perdez 150 points de vie !\n"
        script(entry,0.04,0.5)
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
            script(entry,0.07,0)
            game = False
            start()
        entry ="Vous rebroussez chemin tant bien que mal pour monter les escaliers avec difficulté ...\n"
        script(entry,0.04,1)
   

    entry = "En arrivant à l'étage supérieur,"
    script(entry,0.04,0.5)
    entry = " vous apercevez une ombre bougée au loin dans l'obscurité.\n"
    script(entry,0.04,0.5)
    entry = "Des yeux rouges émanent de cette ombre ...\n"
    script(entry,0.04,0.5)
    entry = "Plus vous vous approchez et plus vous sentez une respiration et un souffle intense venant de la créature.\n"
    script(entry,0.04,1)
    print ("1 - Lancer votre torche pour éclairer la zone 2 - Continuer d'avancer discrètement")
    player_choice = input("> ")
    while player_choice not in ["1","2"]:
        print("Veuillez répondre par 1 ou par 2")
        player_choice = input("> ")
    if player_choice == "1":
        os.system('cls')
        time.sleep(1)
        entry = "« Aaarrggghhh !!"
        script(entry,0.03,0.5)
        entry = " J'ai senti ta puenteur à des kilomètres,"
        script(entry,0.04,0.6)
        entry = " humain. »\n"
        script(entry,0.07,0.5)
        entry = "Le couloir s'éclaircit ...\n"
        script(entry,0.04,1)
        entry = "Vous apercevez un troll mesurant plus de 3 mètres à quelques pas de vous.\n"
        script(entry,0.06,0.7)
        entry = "Le troll piétine votre torche.\n"
        script(entry,0.04,0.5)
        entry = "« Sais tu qui je suis ? »\n"
        script(entry,0.04,1)
        print ("1 - Continuer la discussion 2 - Attaquer le troll")
        player_choice = input("> ")
        while player_choice not in ["1","2"]:
            print("Veuillez répondre par 1 ou par 2")
            player_choice = input("> ")

        if player_choice == "1":
            entry = "- Non je n'en ai pas la moindre idée,"
            script(entry,0.04,0.3)
            entry = " en revanche,"
            script(entry,0.04,0.4)
            entry = " tu ferais mieux de t'écarter de mon chemin vieux troll.\n"
            script(entry,0.04,0.8)
            entry = "Je me nomme Gog'Magog ou devrais-je dire : "
            script(entry,0.03,0.4)
            entry = "Gog'Magog le Terrible !\n"
            script(entry,0.04,0.4)
            entry = "Ne sais tu pas que quiconque ayant essayé de m'affronter a su trouver la mort ?\n"
            script(entry,0.04,0.5)
            entry = "- Je me fiche de qui tu es,"
            script(entry,0.04,0.5)
            entry = " parle moi de ton maître ou je te ferai rejoindre tes victimes !\n"
            script(entry,0.04,0.5)
            entry = "- Tout ce que tu as à savoir est que le mage est sur le point d'accomplir sa prophétie et que je tuerai quiconque tente de l'en empêcher !\n"
            script(entry,0.04,0.6)
            entry = "- Que compte-t-il faire et pourquoi a-t-il tué tant de gens ?\n"
            script(entry,0.04,0.5)
            entry = "- Le maître a tuer tous ces miséreux pour leur pauvre âme.\n"
            script(entry,0.04,0.3)
            entry = "(Une telle nouvelle vous fait réagir,"
            script(entry,0.04,0.4)
            entry = " vous ne pouvez contrôler votre colère et vous décidez de tuer le troll.\n"
            script(entry,0.04,1)

        elif player_choice == "2":
            entry = "Vous attaquez le troll sans vous soucier de son importance.\n"
            script(entry,0.04,0.5)


    elif player_choice == "2":
        entry = "Le troll vous remarque et vous charge !\n"
        script(entry,0.04,1)
    

    
    player_choice = input("Appuyez sur n'importe quelle touche pour débuter le combat : ")
    os.system('cls')

    troll = boss_monsters["troll"]
    boss_monster = Monster(troll, troll['health'],troll["attack"],troll["speed"],troll["xp"],troll["loots"])
    if isinstance(player,Mage):
        start_mage_combat(boss_monster)
    elif isinstance(player,Chasseur):
        start_chasseur_combat(boss_monster)
    elif isinstance(player,Guerrier):
        start_guerrier_combat(boss_monster)

    time.sleep(3)

    entry = "Le troll est vaincu,"
    script(entry,0.04,0.5)
    entry = " vous fouillez le cadavre et découvrez des potions qu'il concoctait avant votre arrivée.\n"
    script(entry,0.04,0.5)
    player.inventory.append("potion de soin supérieure")
    player.inventory.append("potion de force supérieure")
    if isinstance(player,Mage):
        player.inventory.append("potion de mana supérieure")
    elif isinstance(player,Chasseur):
        player.inventory.append("potion d'énergie supérieure")
    entry = "Appuyez sur i pour ouvrir votre inventaire\n"
    script(entry,0.04,0.5)
    player_inventory = input("> ")
    while player_inventory not in ["i"]:
        print("Ouvrez l'inventaire en appuyant sur i")
        player_inventory = input("> ")
    print(player.inventory)

    entry = "Vous prenez soin de ranger ces potions dans votre inventaire et continuez votre route.\n"
    script(entry,0.04,0.5)
    entry = "Un nouveau choix se présente à vous :"
    script(entry,0.04,1)
    entry = " Le couloir se divise en deux parties distinctes.\n"
    script(entry,0.04,1)
    entry = "1 - Aller à gauche 2 - Aller à droite\n"
    script(entry,0.04,0.5)
    player_choice = input("> ")
    while player_choice not in ["1","2"]:
        print("Veuillez répondre par 1 ou par 2")
        player_choice = input("> ")
    if player_choice == "1":
        os.system('cls')
        time.sleep(1)
        entry = "Vous ouvrez la porte de gauche, "
        script(entry,0.04,0.5)
        entry = "une allée sombre se dresse devant vous.\n"
        script(entry,0.04,0.7)
        entry = "En avançant,"
        script(entry,0.04,0.5)
        entry =" sans prêter attention,"
        script(entry,0.04,0.5)
        entry = " vous marchez sur une dalle qui à l'air de s'enfoncer dans le sol.\n"
        script(entry,0.04,0.4)
        entry = "(Encore un piège ...)\n"
        script(entry,0.02,0.5)
        player.health -= 150
        entry = "Vous perdez 150 points de vie !\n"
        script(entry,0.04,0.5)
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
            script(entry,0.07,0)
            game = False
            start()
    elif player_choice == "2":
        os.system('cls')
        time.sleep(1)
        entry = "Vous ouvrez la porte de droite, "
        script(entry,0.04,0.5)
        entry = "une allée claire et vide se dresse devant vous.\n"
        script(entry,0.04,0.7)
        entry = "(L'autre porte devait sûrement être un piège...)\n"
        script(entry,0.04,0.5)

    entry = "Vous rejoignez le bout de l'allée et vous rendez compte que l'autre allée vous aurait fait prendre la même sortie.\n"
    script(entry,0.04,1)
    entry = "L'embouchure à l'air de mener vers un escalier central,"
    script(entry,0.04,0.5)
    entry = " vous montez l'escalier prudemment.\n"
    script(entry,0.04,1)
    entry = "Vous repensez à une chose : "
    script(entry,0.04,0.3)
    entry = ("Le troll n'avait pas l'air assez fort pour pousser un grognement aussi puissant tout à l'heure...\n")
    script(entry,0.04,1)
    entry = "Une pièce se trouve devant vous."
    script(entry,0.04,0.5)
    entry = " Elle s'apparente à une salle de garde.\n"
    script(entry,0.04,0.3)
    entry = "!!!\n"
    script(entry,0.02,1)
    entry = "Un orc immense sort d'un angle mort et tente de vous porter un coup !\n"
    script(entry,0.04,0.5)
    entry = "Vous esquivez le coup de justesse et faites un bon en arrière.\n"
    script(entry,0.04,0.7)
    entry = "Vous : « Ta taille te fait défaut,"
    script(entry,0.04,0.3)
    entry = " orc ! »\n" 
    script(entry,0.04,0.7)
    entry = "- Grrrrroaaarr !!\n"
    script(entry,0.02,0.5)
    entry = "(L'orc n'a pas l'air de savoir parler votre langue)\n"
    script(entry,0.04,0.5)
    
    entry = "Vous prenez les choses en main et contre-attaquez aussi tôt !\n"
    script(entry,0.04,1)

    player_choice = input("Appuyez sur n'importe quelle touche pour débuter le combat : ")
    os.system('cls')
    orc = boss_monsters["orc"]
    boss_monster = Monster(orc, orc['health'],orc["attack"],orc["speed"],orc["xp"],orc["loots"])
    if isinstance(player,Mage):
        start_mage_combat(boss_monster)
    elif isinstance(player,Chasseur):
        start_chasseur_combat(boss_monster)
    elif isinstance(player,Guerrier):
        start_guerrier_combat(boss_monster)

    time.sleep(3)

    entry = "Vous : « Satané créature,"
    script(entry,0.04,0.5)
    entry = " elle m'a finalement donné du fil à retordre ».\n"
    script(entry,0.04,0.5)
    
    entry = "\nVous jetez un coup d'oeil aux alentours et vous apercevez un coffre sur le côté.\n"
    script(entry,0.04,1)
    print("1 - Ouvrir le coffre - 2 Passer votre chemin")
    
    player_choice = input("> ")
    while player_choice not in ["1","2"]:
        print("Veuillez répondre par 1 ou par 2")
        player_choice = input("> ")
    if player_choice == "1":
        os.system('cls')
        time.sleep(1)
        if isinstance(player,Guerrier):
            entry= "Vous découvrez une épée bien plus imposante que la vôtre !\n"
            script(entry,0.04,0.3)
            entry = "Vous vous en équipez de ce pas !\n"
            script(entry,0.04,0.5)
            player.inventory.append("Épée de la garde royale")
            player.current_weapon = end_weapon["épée"]["attack"]
            entry = "En l'inspectant,"
            script(entry,0.04,0.3)
            entry = "vous vous rendez compte qu'il sagit de l'Épée de la garde royale dont vous avez entendu parlé lors de votre aventure.\n"
            script(entry,0.04,0.5)


        elif isinstance(player,Mage):
            entry= "Vous découvrez un baton magique bien plus imposant que le vôtre !\n"
            script(entry,0.04,0.3)
            entry = "Vous vous en équipez de ce pas !\n"
            script(entry,0.04,0.5)
            player.inventory.append("Bâton des milles-tempêtes")
            player.current_weapon = end_weapon["baton"]["attack"]
            entry = "En l'inspectant,"
            script(entry,0.04,0.3)
            entry = "vous vous rendez compte qu'il sagit du Bâton des milles-tempêtes dont vous avez entendu parlé lors de votre aventure.\n"
            script(entry,0.04,0.5)

        elif isinstance(player,Chasseur):
            entry= "Vous découvrez un arc bien plus imposant que le vôtre !\n"
            script(entry,0.04,0.3)
            entry = "Vous vous en équipez de ce pas !\n"
            script(entry,0.04,0.5)
            player.inventory.append("Arc long des gardiens anciens")
            player.current_weapon = end_weapon["arc"]["attack"]
            entry = "En l'inspectant,"
            script(entry,0.04,0.3)
            entry = "vous vous rendez compte qu'il sagit de l'Arc des gardiens anciens dont vous avez entendu parlé lors de votre aventure.\n"
            script(entry,0.04,0.5)

        entry = "Vous trouvez également deux nouvelles potions de soin !\n"
        script(entry,0.04,0.5)
        player.inventory.append("potion de soin mineure")
        player.inventory.append("potion de soin supérieure")
        entry = "Vous vous sentez enfin chanceux dans votre épopée !\n"
        script(entry,0.04,0.5)
        entry = "Il est temps de se remettre en route...\n"

    entry = "L'orc avait l'air de garder cette salle.\n"
    script(entry,0.04,0.5)
    entry = "En revanche, vous ne voyez aucune porte aux alentours...\n"
    script(entry,0.04,0.5)
    entry = "La salle du magicien noir doit se tenir derrière un passage secret.\n"
    script(entry,0.04,1)
    entry = "Vous faites le tour sur vous même et vous apercevez une bibliothèque,"
    script(entry,0.04,0.3)
    entry =" un levier,"
    script(entry,0.04,0.3)
    entry = " des symboles.\n"
    script(entry,0.04,1)

    
    print("1 - Inspecter la bibliothèque sur votre gauche 2 - Activer le levier sur votre droite 3 - Inspecter les symboles au fond de la pièce")
    
    player_choice = input("> ")
    while player_choice not in ["1","2","3"]:
        print("Veuillez répondre par 1, 2 ou 3")
        player_choice = input("> ")
        
    if player_choice == "1":
        os.system('cls')
        time.sleep(1)
        entry = "Vous vous rendez vers la bibliothèque.\n"
        script(entry,0.04,0.5)
        entry = "Vous vient l'idée de pousser et de tirer chaque livre que vous voyez en espérant que cela active un passage."
        script(entry,0.04,0.5)
        entry = " En vain.\n"
        script(entry,0.04,1)
        print("1 Activer le levier de l'autre côté 2 - Inspecter les symboles au fond de la pièce")
        while player_choice not in ["1","2"]:
            print("Veuillez répondre par 1 ou par 2")
            player_choice = input("> ")
            if player_choice == "1":
                entry ="Vous vous rendez alors de l'autre côté et activez le levier en le tirant de toutes vos forces.\n"
                script(entry,0.04,0.5)
                entry = "Étonnement le levier à l'air de fonctionner.\n"
                script(entry,0.04,0.5)
                entry = "Un passage se forme dans un coin de la pièce...\n"
                script(entry,0.04,2)

            elif player_choice == "2":
                entry ="Vous vous rendez au fond de la pièce.\n"
                script(entry,0.04,0.5)
                entry = "Vous essayez de lire les symboles et de les toucher.\n"
                script(entry,0.04,0.3)
                entry = "Un symbole s'enfonce dans le mur.\n"
                script(entry,0.03,0.5)
                entry = "Un bruit rententit dans toute la pièce,"
                script(entry,0.03,0.5)
                entry =" vous vous retournez et constatez qu'un sort d'ombre est lancé sur vous...\n"
                script(entry,0.03,0.5)
                entry = "Vous ne parvenez pas à l'esquiver et perdez 150 points de vie\n"
                script(entry,0.03,0.5)
                player.health -= 150
                if player.health <= 0:
                    entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
                    script(entry,0.07,0)
                    game = False
                    start()
                entry = "Le sort avait l'air de venir de la statue murale accrochée au dessus de l'entrée...\n"
                script(entry,0.03,0.5)
                entry = "Vous ne touchez plus aux symboles sur le mur par peur de subir le même sort.\n"
                script(entry,0.03,0.5)
                entry ="Vous vous rendez alors à votre gauche et activez le levier en le tirant de toutes vos forces.\n"
                script(entry,0.04,0.5)
                entry = "Étonnement le levier à l'air de fonctionner.\n"
                script(entry,0.04,0.5)
                entry = "Un passage se forme dans un coin de la pièce...\n"
                script(entry,0.04,2)

    elif player_choice == "2":
        os.system('cls')
        time.sleep(1)
        entry ="Vous vous rendez alors sur votre droite et activez le levier en le tirant de toutes vos forces.\n"
        script(entry,0.04,0.5)
        entry = "Étonnement le levier à l'air de fonctionner.\n"
        script(entry,0.04,0.5)
        entry = "Un passage se forme dans un coin de la pièce...\n"
        script(entry,0.04,2)



    elif player_choice == "3":
        os.system('cls')
        time.sleep(1)
        entry = "Vous marchez jusqu'au fond de la salle.\n"
        script(entry,0.04,0.5)
        entry = "Vous essayez de lire les symboles et de les toucher.\n"
        script(entry,0.04,0.3)
        entry = "Un symbole s'enfonce dans le mur.\n"
        script(entry,0.03,0.5)
        entry = "Un bruit retentit dans toute la pièce,"
        script(entry,0.03,0.5)
        entry =" vous vous retournez et constatez qu'un sort d'ombre est lancé sur vous...\n"
        script(entry,0.03,0.5)
        entry = "Vous ne parvenez pas à l'esquiver et perdez 150 points de vie.\n"
        script(entry,0.03,0.5)
        player.health -= 150
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
            script(entry,0.07,0)
            game = False
            start()
        entry = "Le sort avait l'air de venir de la statue murale accrochée au dessus de l'entrée...\n"
        script(entry,0.03,0.5)
        entry = "Vous ne touchez plus aux symboles sur le mur par peur de subir le même sort.\n"
        script(entry,0.03,0.5)

        print("1 Inspecter la bibliothèque sur votre droite - Activer le levier sur votre gauche")
        while player_choice not in ["1","2"]:
            print("Veuillez répondre par 1 ou par 2")
            player_choice = input("> ")
            if player_choice == "1":
                entry = "Vous vous rendez vers la bibliothèque.\n"
                script(entry,0.04,0.5)
                entry = "Vous vient l'idée de pousser et de tirer chaque livre que vous voyez en espérant que cela active un passage."
                script(entry,0.04,0.5)
                entry = " En vain.\n"
                script(entry,0.04,1)

                entry ="Vous vous rendez alors de l'autre côté et activez le levier en le tirant de toutes vos forces.\n"
                script(entry,0.04,0.5)
                entry = "Étonnement le levier à l'air de fonctionner.\n"
                script(entry,0.04,0.5)
                entry = "Un passage se forme dans un coin de la pièce...\n"
                script(entry,0.04,2)

    
    entry = "Le passage est long et étroit...\n"
    script(entry,0.04,0.5)
    entry = "Vous vous dirigez vers la sortie de ce passage!\n"
    script(entry,0.04,0.5)
    entry = "...\n\n"
    script(entry,0.5,3)
    os.system('cls')
    time.sleep(2)
    entry = "Le mage noir : «"
    script(entry,0.04,0.8)
    entry = " Te voilà enfin,"
    script(entry,0.04,0.8)
    entry = f" {player_name}.\n"
    script(entry,0.04,0.5)
    entry = "J'ai longtemps attendu ta venue... »"
    script(entry,0.04,0.5)
    entry = " J'ai su que tu te retrouverais devant moi à cet instant.\n"
    script(entry,0.04,1.5)
    print("1 - Comment sait-il ? 2 - Menace !")
    player_choice = input("> ")
    while player_choice not in ["1","2"]:
        print("Veuillez répondre par 1 ou par 2")
        player_choice = input("> ")
    if player_choice == "1":
        entry = "- Comment saviez vous que je serais là ?\n"
        script(entry,0.04,0.3)
        entry = "- Ce n'est pas bien compliqué ..."
        script(entry,0.05,0.5)
        entry = " Je peux tout voir grâce à mes pouvoirs\n"
        script(entry,0.04,0.7)




    elif player_choice == "2":
        entry = "- Vous allez payer pour ce que vous avez fait !\n"
        script(entry,0.05,0.5)
        entry = "- Les menaces ne fonctionnent pas avec moi mon cher.\n"
        script(entry,0.04,0.5)


    entry = "- Pourquoi avoir tué tous ces pauvres innocents ?\n"
    script(entry,0.04,0.5)
    entry = "- Nerathor ne t'a-t-il pas dit qui je suis alors ?\n"
    script(entry,0.04,0.5)
    entry = "- Qu'à-t-il à voir avec tout ça ?\n"
    script(entry,0.04,0.5)
    entry = "- Je vais tout te raconter :\n"
    script(entry,0.04,0.5)
    entry = "Nerathor est mon frère,"
    script(entry,0.03,0.5)
    entry = " à l'époque,"
    script(entry,0.03,0.5)
    entry = " nous étions inséparable.\n"
    script(entry,0.03,0.5)
    entry = "Nous avions à l'époque découvert une magie ancienne appelée Python."
    script(entry,0.03,0.5)
    entry = " Cette magie était terriblement puissante et nous ne voulions plus en entendre parler après avoir vu l'étendue de ce qu'elle pouvait faire.\n"
    script(entry,0.03,0.5)
    entry = "Ce que je ne savais pas,"
    script(entry,0.03,0.5)
    entry = " c'est que Nerathor voulait en être le seul propriétaire.\n"
    script(entry,0.03,0.5)
    entry = "Durant des années,"
    script(entry,0.03,0.5)
    entry = " il essaya d'en prendre le contrôle sans que l'on puisse s'en apercevoir.\n"
    script(entry,0.03,0.5)
    entry = "Un beau jour,"
    script(entry,0.03,0.5)
    entry = " j'ai découvert son secret et essayé de l'en empêcher.\n"
    script(entry,0.03,0.5)
    entry = "Il était trop tard,"
    script(entry,0.03,0.5)
    entry = "Le python avait eu raison de lui et lui avait corrumpu l'esprit.\n"
    script(entry,0.03,0.5)
    entry = "Je suppose qu'il t'a envoyé me tuer mais ce que tu ne sais pas c'est qu'il est l'unique personne à avoir tuer toutes ces personnes.\n"
    script(entry,0.03,0.5)
    entry = "Il a corrompu, tué et transformé des centaines de personnes en différentes créatures.\n"
    script(entry,0.03,0.5)
    entry = "Mes gardes que tu as tué en faisait partie.\n"
    script(entry,0.03,0.5)
    entry = "Il a réussi à convaincre les villages de Eldrida que j'étais le fautif en les manipulant.\n"
    script(entry,0.03,0.5)
    entry= "J'ai donc été accusé d'être le mage noir alors qu'il est l'auteur de ces massacres.\n"
    script(entry,0.03,0.5)
    entry = "La population m'a bannie et je me suis exilé dans ce donjon perdu.\n"
    script(entry,0.03,3)
    entry = "Vous : - Pourquoi alors le gnome, le troll et l'orc m'ont attaqués ?\n"
    script(entry,0.03,0.5)
    entry = "- Je les ai posté là pour qu'ils puissent dissuader quiconque de s'approcher de moi.\n"
    script(entry,0.03,0.5)
    entry = "Tu n'es pas le seul que Nerathor a entrainé pour venir me chercher.\n"
    script(entry,0.03,1)
    entry = "(Vous prenez un moment pour réfléchir à la situation ...).\n"
    script(entry,0.03,1)
    entry = f"- Je te demande de me croire {player_name}.\n"
    script(entry,0.05,2)
    print ("1 - Croire le mage noir 2 - L'attaquer")
    player_choice = input("> ")
    while player_choice not in ["1","2"]:
        print("Veuillez répondre par 1 ou par 2")
        player_choice = input("> ")
    
    
    if player_choice =="2":

        entry = "Tu fais une grave erreur ...\n\n"
        script(entry,0.04,1)
        entry = "D'une manière ou d'une autre,"
        script(entry,0.04,0.5)
        entry = " sans savoir pourquoi ni comment,"
        script(entry,0.04,0.5)
        entry = " le mage noir arrive à vous convaincre..."
        script(entry,0.04,0.5)
    
    
    entry ="- Très bien," 
    script(entry,0.03,0.5)
    entry = " je te crois,"
    script(entry,0.03,0.5)
    entry = " allons chercher Nerathor dans ce cas.\n"
    script(entry,0.03,5)
    os.system('cls')
    entry = "...\n"
    script(entry,0.5,2)
    entry = "Vous prenez la route pour aller au village en compagnie du mage noir.\n"
    script(entry,0.04,0.5)
    entry ="Sur le chemin,"
    script(entry,0.04,0.3)
    entry =" vous apprenez que le mage noir se nomme : Loïc.\n"
    script(entry,0.04,0.5)
    entry ="Il vous raconte ses passes-temps et ce qu'il fait pour tuer le temps dans son donjon.\n"
    script(entry,0.04,0.5)
    entry ="(Son visage vous rappelle quelqu'un mais vous n'arrivez pas à l'identifier...)\n"
    script(entry,0.04,0.5)
    entry ="Arrivé au village,"
    script(entry,0.04,0.5)
    entry = " vous essayez tant bien que mal de protéger le mage noir en clamant son innoncence.\n"
    script(entry,0.04,0.5)
    entry ="Lorsque Nerathor vous voit arriver,"
    script(entry,0.04,0.5)
    entry = " il comprend que vous connaissez désormais la vérité.\n"
    script(entry,0.04,0.5)
    entry ="Une longue discussion a lieu entre les deux frères et le combat démarre...\n"
    script(entry,0.04,2)
    player_choice = input("Appuyez sur n'importe quelle touche pour débuter le combat : ")
    os.system('cls')
    nerathor = boss_monsters["nerathor"]
    boss_monster = Monster(nerathor, nerathor['health'],nerathor["attack"],nerathor["speed"],nerathor["xp"],nerathor["loots"])
    
    if isinstance(player,Mage):
        end_mage_combat(boss_monster)
    elif isinstance(player,Chasseur):
        end_chasseur_combat(boss_monster)
    elif isinstance(player,Guerrier):
        end_guerrier_combat(boss_monster)
        


def boucle():           #Boucle du jeu (Affiche la map puis les déplacements à effectuer)

    print("Vous voilà au village de Valdrindor")
    print ("Votre personnage se trouve sur le point jaune fluo")
    print ("Voici une visualisation de la carte de haut : ")
    global game
    global map
    global largeur
    largeur = 10
    nb_village = 2
    map = creation_map(largeur,nb_village)           #la map est basé sur un 10 x 10 avec 2 villages et un donjon, possibilité de modifier ces valeurs
    affichage_map(map,largeur)
    satisfied = False 
    while satisfied == False:
        print ("Voulez vous générer une nouvelle carte ?\n 1 - oui / 2 - non")          #Possibilité de générer une nouvelle map si besoin
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
                os.system('cls')
                dungeon_scenario()
            elif player_choice == "2":
                pass
        elif isinstance(map[map[-1]],int):
            village()

        



def start():                                            # Menu de départ
    print("+" + "-"*36 + "+")
    print("|" + " "*36 + "|")
    print("|" + " "*7 + "Bienvenue dans Eldrida" + " "*7 + "|")
    print("|" + " "*36 + "|")
    print("|" + " "*7 + "- 1 Create New Game -" + " "*8 + "|")
    print("|" + " "*12 + "- 2 Rules -" + " "*13 + "|")
    print("|" + " "*12 + "- 3 About -" + " "*13 + "|")
    print("|" + " "*12 + "- 4 Exit  -" + " "*13 + "|")
    print("|" + " "*36 + "|")
    print("+" + "-"*36 + "+")
    title_screen_selections()


def title_screen_selections():                            # choix du menu de départ
    print ("Que voulez vous faire ? ")
    option = input("> ")
    while option.lower() not in ["1","2","3","4"]:
        print ("Veuillez insérer une commande valide.")
        option = input("> ")
    if option.lower() == "1":
        start_game()
    elif option.lower() =="2":
        rules()
    elif option.lower() == "3":
        about_menu()
    elif option.lower() == "4":
        print ("Etes-vous sûr de vouloir quitter ? \n1 - oui / 2 - non")
        option = input ("> ")
        while option.lower() not in ["1","2"]:
            print("Veuillez choisir entre 1 et 2")
            option = input ("> ")
        if option.lower() == "1":
            sys.exit()
        elif option.lower() == "2":
            start()

def set_player_attribute():                              #attributs du joueur : sexe, classe 
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
    print("+" + "-"*50 + "+")
    print("|" + " "*14 + "- Choix de la classe -" + " "*14 + "|")
    print("|" + " "*50 + "|")
    print("|" + " "*6 +"1 - Guerrier   2 - Mage   3 - Chasseur" + " "*6 + "|") 
    print("|" + " "*50 + "|")
    print("+" + "-"*50 + "+")
    player = input("> ")
    while player.lower() not in ["1","2","3"]:
        print("Veuillez sélectionner une classe")
        player = input("> ")
    if player.lower() == "1":
        player = Guerrier()
        if player_gender.lower() == "h":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " valeureux guerrier !\n"
            script(entry,0.04,2)
        elif player_gender.lower() == "f":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " valeureuse guerrière !\n"
            script(entry,0.04,2)
    elif player.lower() == "2":
        player = Mage()
        if player_gender.lower() == "h":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " le noble mage !\n"
            script(entry,0.04,2)
        elif player_gender.lower() == "f":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " la noble mage !\n"
            script(entry,0.04,2)
    elif player.lower() == "3":
        player = Chasseur()
        if player_gender.lower() == "h":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " le chasseur intrépide"
            script(entry,0.04,2)
        elif player_gender.lower() == "f":
            entry = f"Bonne chance dans votre aventure {player_name},"
            script(entry,0.04,0.5)
            entry = " la chasseuse intrépide"
            script(entry,0.04,2)
    os.system("cls")


def start_game():                       #fonction complète du jeu regroupant le scénario du début + les attribus du joueur + la boucle de jeu
    story()
    set_player_attribute()
    boucle()

def rules():                             #règle du jeu

    print("+" + "-"*197 + "+")
    print("|" + " "*9 + "Les règles" + " "*178 + "|")
    print("|" + " "*197 + "|")
    print("|" + " "*9 + "-  Vous avez le choix entre 3 classes différentes pour débuter : -" + " "*122 + "|")
    print("|" + " "*9 + "-  Guerrier (Commence la partie avec une épée, le guerrier gagne de la furie en attaquant ses ennemies, il peut ensuite consommer cette furie pour assainer de puissants coups ! -" + " "*10 + "|")
    print("|" + " "*9 + "-  Mage     (Commence la partie avec un baton magique, il peut consommer sa mana pour lancer des boules de feu, bien plus puissantes que ses simples projectiles de glace ! -" + " "*15 + "|")
    print("|" + " "*9 + "-  Chasseur (Commence la partie avec un arc, il peut consommer son énergie pour lancer des coups multiples, bien plus puissants que ses simples flèches ! -" + " "*33 + "|")
    print("|" + " "*9 + "-  Votre but est de trouver le donjon caché dans la forêt -" + " "*129 + "|")
    print("|" + " "*9 + "-  Les F en blanc sont les zones inexplorées de la carte, les f en vert sont les zones explorées de la carte. -" + " "*77 + "|")
    print("|" + " "*9 + "-  Les chiffres représentent les villages et le D représente le donjon. -" + " "*115 + "|")
    print("|" + " "*197 + "|")
    print("+" + "-"*197 + "+")
    
    print("\n\nAppuyez sur n'importe quelle touche pour revenir au menu")
    answer = input("> ")
    start()
    title_screen_selections()
    


def about_menu():          #Menu à propos (Le nom du jeu étant Eldrida)
    print("+" + "-"*50 + "+")
    print("|" + " "*50 + "|")
    print("|" + " "*15 + "A propos de Eldrida" + " "*16 + "|")
    print("|" + " "*50 + "|")
    print("|" + " "*11 + "Eldrida est un RPG textuel" + " "*13 + "|")
    print("|" + " "*10 + "codé entièrement en python et" + " "*11 + "|")
    print("|" + " "*11 + "réalisé par Joffrey Gaucher," + " "*11 + "|")
    print("|" + " "*11 + "Adrien Formoso, Nathan Luu," + " "*12 + "|")
    print("|" + " "*12 + "étudiants en web et data" + " "*14 + "|")
    print("|" + " "*15 + "1ere année à Hetic" + " "*17 + "|")
    print("|" + " "*50 + "|")
    print("|" + " "*19 + "Version 1.0" + " "*20 + "|")
    print("|" + " "*50 + "|")
    print("|" + " "*18 + "Copyright 2023" + " "*18 + "|")
    print("|" + " "*50 + "|")
    print("+" + "-"*50 + "+")
    print("\n\nAppuyez sur n'importe quelle touche pour revenir au menu")
    answer = input("> ")
    start()
    title_screen_selections()


def check_potion():                 #check pour savoir si le joueur a des potions + les utiliser et afficher leurs effets.
    
    
    if "potion de soin mineure" not in player.inventory and "potion de soin supérieure"not in player.inventory and "potion de force mineure"not in player.inventory and "potion de soin supérireure"not in player.inventory and "potion de mana mineure"not in player.inventory and "potion de mana supérireure"not in player.inventory and "potion d'énergie mineure"not in player.inventory and "potion d'énergie supérieure" not in player.inventory:
        return
    print("Voulez vous : 1 - Utiliser une potion / 2 - Combattre")
    player_choice = input("> ")
    while player_choice not in ["1","2"]:
        print("Veuillez choisir entre 1 - utiliser une potion ou 2 - combattre")
        player_choice = input("> ")
    if player_choice == "2":
        return
    elif player_choice == "1":
        
        print ("Voulez vous :\n1) Utiliser une potion de soin\n2) Utiliser une potion de mana / énergie\n3) Utiliser une potion de force\n4) Retour")
        player_choice = input ("> ")
        while player_choice.lower() not in ["1","2","3","4"]:
            print ("Veuillez choisir entre 1 - utiliser une potion de soin 2 - utiliser une potion de mana / énergie ou 3 - utiliser une potion de force")
            player_choice = input ("> ")
        if player_choice =="4":
            check_potion()
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
                        print("Vous récupérez 150 points de vie")
                        player.health += 150
                        if player.health > player.max_health:
                            player.health = player.max_health
                elif health_pot_check == "2":
                    player.inventory.remove("potion de soin supérieure")
                    player.health += 300
                    print("Vous récupérez 300 points de vie")

                    if player.health > player.max_health:
                        player.health = player.max_health
            elif "potion de soin mineure" in player.inventory and "potion de soin supérieure" not in player.inventory:
                print ("Vous ne possédez pas de potion de soin supérieure\nUtilisation d'une potion de soin mineure")
                player.inventory.remove("potion de soin mineure")
                player.health += 150
                print("Vous récupérez 150 points de vie")
                
                if player.health > player.max_health:
                    player.health = player.max_health
            elif "potion de soin mineure" not in player.inventory and "potion de soin supérieure" in player.inventory:
                print ("Vous ne possédez pas de potion de soin mineure\nUtilisation d'une potion de soin supérieure")
                player.inventory.remove("potion de soin supérieure")
                player.health += 300
                print("Vous récupérez 150 points de vie")

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
                            print("Vous récupérez 30 points de mana")

                            if player.mana >player.max_mana:
                                player.mana =player.max_mana
                    elif health_pot_check == "2":
                        player.inventory.remove("potion de mana supérieure")
                        player.mana += 50
                        print("Vous récupérez 50 points de mana")

                        if player.mana >player.max_mana:
                            player.mana =player.max_mana
                elif "potion de mana mineure" in player.inventory and "potion de mana supérieure" not in player.inventory:
                    print ("Vous ne possédez pas de potion de mana supérieure\nUtilisation d'une potion de mana mineure")
                    player.inventory.remove("potion de mana mineure")
                    player.mana += 30
                    print("Vous récupérez 30 points de mana")

                    if player.mana >player.max_mana:
                        player.mana =player.max_mana
                elif "potion de mana mineure" not in player.inventory and "potion de mana supérieure" in player.inventory:
                    print ("Vous ne possédez pas de potion de mana mineure\nUtilisation d'une potion de mana supérieure")
                    player.inventory.remove("potion de mana supérieure")
                    player.mana += 50
                    print("Vous récupérez 50 points de mana")

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
                            print("Vous récupérez 30 points d'énergie")

                            if player.energy >player.max_energy:
                                player.energy =player.max_energy
                    elif health_pot_check == "2":
                        player.inventory.remove("potion d'énergie supérieure")
                        player.energy += 50
                        print("Vous récupérez 50 points d'énergie")

                        if player.energy >player.max_energy:
                            player.energy =player.max_energy
                elif "potion d'énergie mineure" in player.inventory and "potion d'énergie supérieure" not in player.inventory:
                    print ("Vous ne possédez pas de potion d'énergie supérieure\nUtilisation d'une potion d'énergie mineure")
                    player.inventory.remove("potion d'énergie mineure")
                    player.energy += 30
                    print("Vous récupérez 30 points d'énergie")

                    if player.energy >player.max_energy:
                        player.energy =player.max_energy
                elif "potion d'énergie mineure" not in player.inventory and "potion d'énergie supérieure" in player.inventory:
                    print ("Vous ne possédez pas de potion d'énergie mineure\nUtilisation d'une potion d'énergie supérieure")
                    player.inventory.remove("potion d'énergie supérieure")
                    player.energy += 50
                    print("Vous récupérez 50 points d'énergie")

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
                        print("Vous gagnez 10 points d'attaque")
                        if player.health > player.max_health:
                            player.health = player.max_health
                elif health_pot_check == "2":
                    player.inventory.remove("potion de force supérieure")
                    player.attack += 30
                    print("Vous gagnez 30 points d'attaque")

                    if player.health > player.max_health:
                        player.health = player.max_health
            elif "potion de force mineure" in player.inventory and "potion de force supérieure" not in player.inventory:
                print ("Vous ne possédez pas de potion de force supérieure\nUtilisation d'une potion de force mineure")
                player.inventory.remove("potion de force mineure")
                player.attack += 10
                print("Vous gagnez 10 points d'attaque")

                if player.health > player.max_health:
                    player.health = player.max_health
            elif "potion de force mineure" not in player.inventory and "potion de force supérieure" in player.inventory:
                print ("Vous ne possédez pas de potion de force mineure\nUtilisation d'une potion de force supérieure")
                player.inventory.remove("potion de force supérieure")
                player.attack += 30
                print("Vous gagnez 30 points d'attaque")
            

                if player.health > player.max_health:
                    player.health = player.max_health
                     

def loot(monster):                  # 3 chance sur 4 de loot un objet venant du monstre aléatoire. 
        loot = random.randint(0,100)
        if loot >= 25:
            player_loot = random.choice(list(monster.loot))
            print (f"Vous fouillez le cadavre et vous trouvez : {player_loot} \nL'objet a été ajouté à votre inventaire...")
            player.inventory.append(player_loot)
        else:
            print("Vous ne trouvez rien sur le cadavre")

def start_combat():               #La fonction sélectionne un monstre de la classe Monstre qui sera aléatoire puis en fonction de l'instance de la classe du joueur, envoi la bonne fonction de combat

    monster = Monster()
    
    player.attack = player.max_attack
    print (f"Un ennemi approche ! C'est un(e) {monster.type}")
    print ("Souhaitez vous : 1 - combattre / 2 - fuir ?")
    player_choice = input("> ")
    while player_choice.lower() not in ["1","2"]:
        print("Veuillez taper 1 pour combattre, 2 pour fuir")
        player_choice = input("> ")
    if player_choice.lower() == "2":
        escape = random.randint(0,100)                              #possibilité de fuir le combat en fonction de la chance de base de notre classe
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

def start_guerrier_combat(monster):                                     #fonction pour le combat du guerrier
    global game
    player.fury = 0
    
    print ("-------------------------------------------")
    print (f"VOS HP : {player.health} / {player.max_health}     |    HP DE L'ENNEMI : {monster.health}")
    print ("-------------------------------------------")
    
    
    if player.speed <= monster.speed:
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("L'ennemi(e) attaque en premier !")
        player.health -= monster.attack
        print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
            script(entry,0.07,0)
            game = False
            start()
        else:
            print (f"Il vous reste {player.health} HP")
    else:
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
                    entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
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
                        entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
                        script(entry,0.07,0)
                        game = False
                        start()
                    else :
                        print (f"Il vous reste {player.health} HP")

                elif player_choice == "2":

                    player.fury += 40
                    if player.fury > 100:
                        player.fury = 100
                    print (f'Évocation ! Votre furie est désormais de {player.fury}')
                    
                    player.health -= monster.attack
                    print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
                    if player.health <= 0:
                        entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
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
                    entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
                    script(entry,0.07,0)
                    start()
                else :
                    print(f"Il vous reste {player.health} HP")
                    
            elif player_choice == "2":

                player.fury += 40
                if player.fury > 100:
                    player.fury = 100
                print (f'Évocation ! Votre furie est désormais de {player.fury}')
                
                player.health -= monster.attack
                print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
                
                if player.health <= 0:
                    entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
                    script(entry,0.07,0)
                    start()
                else :
                    print (f"Il vous reste {player.health} HP")
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
    
    if map[-1] == map[-2]:
        return
    affichage_map(map,largeur)


            
def start_chasseur_combat(monster):                     #fonction pour le combat du chasseur
    global game

    print ("-------------------------------------------")
    print (f"VOS HP : {player.health} / {player.max_health}    |    HP DE L'ENNEMI : {monster.health}")
    print ("-------------------------------------------")
    
    if player.speed <= monster.speed:
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("L'ennemi(e) attaque en premier !")
        player.health -= monster.attack
        print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
            script(entry,0.07,0)
            game = False
            start()
        else:
            print (f"Il vous reste {player.health} HP")
    else:
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
                player.energy += 10
                
            if monster.health <= 0:
                print(f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                break
            else :
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')
                    
            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
            if player.health <= 0:
                entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
                script(entry,0.07,0)
                start()
            else:
                print (f"Il vous reste {player.health} HP")
        else:
            print (f"Votre énergie est de {player.energy}, vous n'avez pas assez pour lancer vos flèches multiples !")
            print ("Tir de flèche !")
            player_attack = player.attack
            monster.health -= player_attack
            player.energy += 10
            if monster.health <= 0:
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                print(f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                break
            else :
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')

            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
            
            if player.health <= 0:
                entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
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
        
    if map[-1] == map[-2]:
        return
    affichage_map(map,largeur)
    



def start_mage_combat(monster):                         #fonction pour le combat du mage
    global game
    
    print ("-------------------------------------------")
    print (f"VOS HP : {player.health} / {player.max_health}     |    HP DE L'ENNEMI : {monster.health}")
    print ("-------------------------------------------")


    if player.speed <= monster.speed:
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("L'ennemi(e) attaque en premier !")
        player.health -= monster.attack
        print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
            script(entry,0.07,0)
            game = False
            start()
        else:
            print (f"Il vous reste {player.health} HP")
    else:
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
                
                    
            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
            if player.health <= 0:
                entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
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
                

            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
            
            if player.health <= 0:
                entry = "Vous succombez de vos blessures !!! \nGame over !\n\n"
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

    if map[-1] == map[-2]:
        return
    affichage_map(map,largeur)



def village ():                         # FONCTION QUAND ON RENTRE DANS UN VILLAGE
    
    print("+" + "-"*45 + "+")
    print("|" + " "*14 + "Options du village" + " "*13 + "|")
    print("|" + " "*45 + "|")
    print("|" + " "*9 + "-  1      Boutique        -   " + " "*6 + "|")
    print("|" + " "*9 + "-  2       Repos          -   " + " "*6 + "|")
    print("|" + " "*9 + "-  3  Quitter le village  -   " + " "*6 + "|")
    print("|" + " "*45 + "|")
    print("+" + "-"*45 + "+")
    village_screen_selection()


def village_screen_selection():
    
         # FONCTION POUR DEMANDER AU JOUEUR CE QU IL VEUT FAIRE DANS LE VILLAGE
    print("Que voulez vous faire ?")
    option = input("> ")
    while option.lower() not in ["1","2","3"]:
        print ("Veuillez insérer une commande valide.")
        option = input("> ")
    if option.lower() == "1":

        menu_boutique()
    elif option.lower() == "2":
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


    elif option.lower() == "3":
        print ("Etes-vous sûr de vouloir quitter le village? \n 1 - oui / 2 - non")
        option = input ("> ")
        while option.lower() not in ["1","2"]:
            print("Veuillez choisir entre 1 et 2")
            option = input ("> ")
        if option.lower() == "1":
            os.system('cls')
            affichage_map(map,largeur)
            return
        elif option.lower() == "2":
            village()







def end_guerrier_combat(monster):                                     #fonction pour le dernier combat du guerrier (même que celle du guerrier sauf  player.health <= 0 est différent
    global game
    player.fury = 0
    
    print ("-------------------------------------------")
    print (f"VOS HP : {player.health} / {player.max_health}     |    HP DE L'ENNEMI : {monster.health}")
    print ("-------------------------------------------")
    
    
    if player.speed <= monster.speed:
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("L'ennemi(e) attaque en premier !")
        player.health -= monster.attack
        print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!!\n\n"
            script(entry,0.05,0.5)
            entry = "..."
            script(entry,0.5,0.5)
            entry = "Vous ouvrez les yeux,"
            script(entry,0.04,0.5)
            entry = " vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
            script(entry,0.04,0.5)
            entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
            script(entry,0.04,0.5)
            entry = "Tout ça n'était qu'un rêve...\n"
            script(entry,0.04,3)
            game = False
            start()
        else:
            print (f"Il vous reste {player.health} HP")
    else:
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
                    entry = "Vous succombez de vos blessures !!!\n\n"
                    script(entry,0.05,0.5)
                    entry = "..."
                    script(entry,0.5,0.5)
                    entry = "Vous ouvrez les yeux,"
                    script(entry,0.04,0.5)
                    entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
                    script(entry,0.04,0.5)
                    entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
                    script(entry,0.04,0.5)
                    entry = "Tout ça n'était qu'un rêve...\n"
                    script(entry,0.04,3)
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
                        entry = "Vous succombez de vos blessures !!!\n\n"
                        script(entry,0.05,0.5)
                        entry = "..."
                        script(entry,0.5,0.5)
                        entry = "Vous ouvrez les yeux,"
                        script(entry,0.04,0.5)
                        entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
                        script(entry,0.04,0.5)
                        entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
                        script(entry,0.04,0.5)
                        entry = "Tout ça n'était qu'un rêve...\n"
                        script(entry,0.04,3)
                        game = False
                        start()

                    else :
                        print (f"Il vous reste {player.health} HP")

                elif player_choice == "2":

                    player.fury += 40
                    if player.fury > 100:
                        player.fury = 100
                    print (f'Évocation ! Votre furie est désormais de {player.fury}')
                    
                    player.health -= monster.attack
                    print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")

                    if player.health <= 0:
                        entry = "Vous succombez de vos blessures !!!\n\n"
                        script(entry,0.05,0.5)
                        entry = "..."
                        script(entry,0.5,0.5)
                        entry = "Vous ouvrez les yeux,"
                        script(entry,0.04,0.5)
                        entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
                        script(entry,0.04,0.5)
                        entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
                        script(entry,0.04,0.5)
                        entry = "Tout ça n'était qu'un rêve...\n"
                        script(entry,0.04,3)
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
                    entry = "Vous succombez de vos blessures !!!\n\n"
                    script(entry,0.05,0.5)
                    entry = "..."
                    script(entry,0.5,0.5)
                    entry = "Vous ouvrez les yeux,"
                    script(entry,0.04,0.5)
                    entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
                    script(entry,0.04,0.5)
                    entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
                    script(entry,0.04,0.5)
                    entry = "Tout ça n'était qu'un rêve...\n"
                    script(entry,0.04,3)
                    game = False
                    start()
                
              
                else :
                    print(f"Il vous reste {player.health} HP")
                    
            elif player_choice == "2":

                player.fury += 40
                if player.fury > 100:
                    player.fury = 100
                print (f'Évocation ! Votre furie est désormais de {player.fury}')
                
                player.health -= monster.attack
                print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
                
                if player.health <= 0:
                    entry = "Vous succombez de vos blessures !!!\n\n"
                    script(entry,0.05,0.5)
                    entry = "..."
                    script(entry,0.5,0.5)
                    entry = "Vous ouvrez les yeux,"
                    script(entry,0.04,0.5)
                    entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
                    script(entry,0.04,0.5)
                    entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
                    script(entry,0.04,0.5)
                    entry = "Tout ça n'était qu'un rêve...\n"
                    script(entry,0.04,3)
                    game = False
                    start()

                else :
                    print (f"Il vous reste {player.health} HP")
    if monster.health <= 0:

        if player.level == 20:
            pass
        else:
            player.xp += monster.xp
            print (f"Vous obtenez {monster.xp} points d'expériences ! ")
            if player.xp >= player.xp_to_lvl_up:
                player.level_up()
            
            print (f"Vous êtes à {player.xp} / {player.xp_to_lvl_up} points d'expérience pour le prochain niveau.")
                
            print ("Félicitation ! Vous avez gagné !")
            time.sleep(3)
            start()





def end_mage_combat(monster):             #fonction pour le combat de fin du mage 
    global game
    print ("-------------------------------------------")
    print (f"VOS HP : {player.health} / {player.max_health}     |    HP DE L'ENNEMI : {monster.health}")
    print ("-------------------------------------------")


    if player.speed <= monster.speed:
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("L'ennemi(e) attaque en premier !")
        player.health -= monster.attack
        print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")


        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!!\n\n"
            script(entry,0.05,0.5)
            entry = "..."
            script(entry,0.5,0.5)
            entry = "Vous ouvrez les yeux,"
            script(entry,0.04,0.5)
            entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
            script(entry,0.04,0.5)
            entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
            script(entry,0.04,0.5)
            entry = "Tout ça n'était qu'un rêve...\n"
            script(entry,0.04,3)
            game = False
            start()

        else:
            print (f"Il vous reste {player.health} HP")
    else:
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
                
                    
            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")


            if player.health <= 0:
                entry = "Vous succombez de vos blessures !!!\n\n"
                script(entry,0.05,0.5)
                entry = "..."
                script(entry,0.5,0.5)
                entry = "Vous ouvrez les yeux,"
                script(entry,0.04,0.5)
                entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
                script(entry,0.04,0.5)
                entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
                script(entry,0.04,0.5)
                entry = "Tout ça n'était qu'un rêve...\n"
                script(entry,0.04,3)
                game = False
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
                

            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
            
            if player.health <= 0:
                entry = "Vous succombez de vos blessures !!!\n\n"
                script(entry,0.05,0.5)
                entry = "..."
                script(entry,0.5,0.5)
                entry = "Vous ouvrez les yeux,"
                script(entry,0.04,0.5)
                entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
                script(entry,0.04,0.5)
                entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
                script(entry,0.04,0.5)
                entry = "Tout ça n'était qu'un rêve...\n"
                script(entry,0.04,3)
                game = False
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
                
            print ("Félicitation, vous avez gagné ! ")
            time.sleep(3)
            start()







def end_chasseur_combat(monster):                     #fonction pour le combat du chasseur de fin 
    global game

    print ("-------------------------------------------")
    print (f"VOS HP : {player.health} / {player.max_health}    |    HP DE L'ENNEMI : {monster.health}")
    print ("-------------------------------------------")
    
    if player.speed <= monster.speed:
        print (f"Votre vitesse est de : {player.speed} ----- Celle de votre ennemi(e) est de : {monster.speed}")
        print ("L'ennemi(e) attaque en premier !")
        player.health -= monster.attack
        print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")


        if player.health <= 0:
            entry = "Vous succombez de vos blessures !!!\n\n"
            script(entry,0.05,0.5)
            entry = "..."
            script(entry,0.5,0.5)
            entry = "Vous ouvrez les yeux,"
            script(entry,0.04,0.5)
            entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
            script(entry,0.04,0.5)
            entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
            script(entry,0.04,0.5)
            entry = "Tout ça n'était qu'un rêve...\n"
            script(entry,0.04,3)
            game = False
            start()

        else:
            print (f"Il vous reste {player.health} HP")
    else:
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
                player.energy += 10
                
            if monster.health <= 0:
                print(f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                break
            else :
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')
                    
            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")


            if player.health <= 0:
                entry = "Vous succombez de vos blessures !!!\n\n"
                script(entry,0.05,0.5)
                entry = "..."
                script(entry,0.5,0.5)
                entry = "Vous ouvrez les yeux,"
                script(entry,0.04,0.5)
                entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
                script(entry,0.04,0.5)
                entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
                script(entry,0.04,0.5)
                entry = "Tout ça n'était qu'un rêve...\n"
                script(entry,0.04,3)
                game = False
                start()

            else:
                print (f"Il vous reste {player.health} HP")
        else:
            print (f"Votre énergie est de {player.energy}, vous n'avez pas assez pour lancer vos flèches multiples !")
            print ("Tir de flèche !")
            player_attack = player.attack
            monster.health -= player_attack
            player.energy += 10
            if monster.health <= 0:
                print ("Vous triomphez ! Votre ennemi(e) est mort !")
                print(f"Vous avez retiré {player_attack} points de vie à votre ennemi !")
                break
            else :
                print (f'Vous avez retiré {player_attack} points de vie à votre ennemi ! Il lui reste {monster.health} HP')

            player.health -= monster.attack
            print (f"L'ennemi(e) vous inflige {monster.attack} points de dégât !")
            

            if player.health <= 0:
                entry = "Vous succombez de vos blessures !!!\n\n"
                script(entry,0.05,0.5)
                entry = "..."
                script(entry,0.5,0.5)
                entry = "Vous ouvrez les yeux,"
                script(entry,0.04,0.5)
                entry = "Vous vous rendez compte que vous étiez entrain de dormir devant votre ordinateur.\n"
                script(entry,0.04,0.5)
                entry = "Votre devoir sur le RPG Python vous a joué des tours.\n"
                script(entry,0.04,0.5)
                entry = "Tout ça n'était qu'un rêve...\n"
                script(entry,0.04,3)
                game = False
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
            print ("Félicitation, vous avez gagné ! ")
            time.sleep(3)
            start()

        


def show_boutique():                                        #la liste des objets disponible
    print("Objets disponibles dans la boutique:")
    i=1
    for item_name, item_info in items.items():
      print(i," "*(2-len(str(i))),")",item_info['name']," "*(24-len(item_info['name'])),":",item_info['price']," "*(3-len(str(item_info['price']))),"pièce(s) d'or - Stock :",item_info['stock'])
      i = i + 1

def menu_argent_dispo(money):                              # afficher l'argent du joueur
    print("+" + "-"*35 + "+")
    print("|" + " "*5 + "Vous avez " + str(money) + " pièce(s) d'or" + " "*5 + "|")
    print("+" + "-"*35 + "+")


def nb_max_liste(liste):        
  i = 0
  for valeur in liste:
    i = i + 1
  return i

def creation_nb_liste(nombre_de_fois):                    # les choix possible d'achat dans une liste
  i = 1
  liste_final = []
  while nombre_de_fois >= i:
    liste_final.append(str(i))
    i = i + 1
  return liste_final

def menu_boutique():          #Affichage des options de la boutique
    global affichage_map
    print("+" + "-"*40 + "+")
    print("|" + " "*9 + "1. Acheter un objet" + " "*12 + "|")
    print("|" + " "*40 + "|")
    print("|" + " "*9 + "2. Vendre un objet" + " "*13 + "|")
    print("|" + " "*40 + "|")
    print("|" + " "*9 + "3. Quitter la boutique" + " "*9 + "|")
    print("+" + "-"*40 + "+")
    menu_argent_dispo(player.money)
    if selection_boutique():                                                    # True = sortir du menu boutique
      return
    else:
      menu_boutique()


def selection_boutique():      #permet de sélectionner les menus de la boutique
  option = input("> ")
  while option not in ["1","2","3"]:
    print("Veuillez insérez une bonne valeur")
    option = input("> ")

  if option == "3":
    affichage_map(map,largeur)
    return True
    

  elif option =="2":
    sell_loot()
    

  elif option == "1":
    selection_achat_objet()
    return False

def selection_achat_objet():    #Regroupe toutes les fonctions pour effectuer l'achat au complet 
    show_boutique()
    valeur_en_liste = list(items.values())
    menu_argent_dispo(player.money)
    print("\nQuel objet désirez-vous acheter ?")
    print("Vous pouvez taper \"retour\" pour revenir en arriere")
    option = input("> ")
    liste_bonne_reponse = creation_nb_liste(nb_max_liste(valeur_en_liste))

    while option not in liste_bonne_reponse:
      if option.lower() == "retour":
        return
      print("\nMerci de renseigner la bonne valeur")
      option = input("> ")

    if option.lower() =="retour":
      return
      
    option = int(option)
    if verification_stock(option, valeur_en_liste):
      if verification_fonds(player.money,option,valeur_en_liste): # verifier si le joueur a assez d'argent
        validation_selection(option,valeur_en_liste)
        return False
      else:
        print("Vous n'avez pas assez de fonds ...")
    else:
      print("Cet objet n'est plus en stock")

def verification_fonds(money,choix,valeur_en_liste):          #Vérifier si le joueur a assez d'argent
  if money >= valeur_en_liste[choix-1]["price"]:
    return True
  else:
    return False

def verification_stock(choix,valeur_en_liste):        #Vérifier si le stock est bon
  if valeur_en_liste[choix-1]["stock"] > 0 :
    return True
  else:
    return False

def validation_selection(choix,valeur_en_liste):         #Fonction pour confirmer l'achat 
  print("\nVoulez-vous acheter :",valeur_en_liste[choix-1]["name"],"pour un montant de",valeur_en_liste[choix-1]["price"],"pièce(s) d'or ?")
  print("1 = oui | 2 = non")
  option = input("> ")
  while option not in ["1","2"]:
      print("\nMerci de renseigner la bonne valeur ")
      option = input("> ")

  if option == "2":
    selection_achat_objet()
    return False

  else:
    item = valeur_en_liste[choix-1]
    player.inventory.append(item["name"])
    player.money-=item["price"]
    item["stock"]-=1
    print("\nVous venez d'acheter",item["name"])
    if hasattr(item,"attack"):                         #si la propriété attack existe, ça veut dire que c'est une arme donc on équipe l'arme + attribue l'attaque à la variable attack du joueur
      if(item["type"] == type(player).__name__):
        print("Vous vous en équipez")
        player.current_weapon = item["attack"]
      else:
        print("Vous ne pouvez pas vous en équiper")
    pass



def sell_loot():        #Fonction pour vendre les objets droppés par les mobs

    print("Vous ne pouvez vendre que des objets ramassés sur des ennemi(e)s ou les armes.")
    print("Inventaire: ", player.inventory)
    item = input("Quel objet voulez-vous vendre? \n>")
    if item in player.inventory:
        if item in global_loot:
            player.inventory.remove(item)
            player.money += global_loot[item]
            print(f"Vous avez vendu {item} pour {global_loot[item]} pièce(s) d'or")
            
        else:
            print("Cet objet ne peut pas être vendu car il n'est pas un loot de monstre.")
    else:
        print("Cet objet n'est pas présent dans votre inventaire.")
    print ("\nSouhaitez vous vendre un autre objet ?\n1 - oui 2 - non")
    player_choice = input("> ")
    while player_choice not in ["1","2"]:
        print("Veuillez sélection un nombre entre 1 et 2")
        player_choice = input("> ")
    if player_choice =="1":
        sell_loot()
    else:   
        return

start()