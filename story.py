from utils import script
import time
import os 

def story ():
    global player_name
    # »  «
    print("Voulez vous passer le scénario ?  1 - oui / 2 - non")
    player_answer = input("> ")
    while player_answer not in ["1","2"]:
        print("Veuillez répondre par 1 ou par 2")
        player_answer = input("> ")
    if player_answer == "1":
        print("Veuillez insérer votre nom d'aventurier : ")
        player_name = input("")
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
        entry = "A l'avant se trouvent deux hommes vêtus tous deux d'une capuche,"
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
        entry = " vous apprenez que la moitié du village à disparu à cause d'un sorcier maléfique.\n"
        script(entry,0.04,0.5)
        entry = "Nul ne sait qui se cache derrière son identité,"
        script(entry,0.04,0.3)
        entry = " mais un but vous a été confié : \n"
        script(entry,0.04,1)
        entry = "Vous devez arrêter la propagation du mal.\n\n"
        script(entry,0.06,2)
        
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

    

    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    




