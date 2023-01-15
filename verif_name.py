

def verif_pseudo(pseudo_origine):       #fonction pour restreindre le nom à ne contenir que des lettres
    liste_caractere_autorise = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']
    taille_minim = 3            #taille du pseudo entre 3 et 15 car
    taille_max = 15
    critere_respecte = False

    pseudo = pseudo_origine.lower()
    while not critere_respecte:
        bon_carac_pseudo = verif_carac_pseudo(pseudo,liste_caractere_autorise)
        bon_taille_pseudo = verif_taille_pseudo(pseudo,taille_minim,taille_max)

        if bon_carac_pseudo and bon_taille_pseudo :
            critere_respecte = True
        
        else:
            print("Votre nom doit être compris entre",taille_minim,"et",taille_max,"caractères et ne pas contenir de caractères spéciaux.")
            pseudo_origine = input("> ")
            pseudo = pseudo_origine.lower()
        
    return pseudo_origine

def verif_carac_pseudo(pseudo,liste_caractere_autorise):
    liste_caractere_non_autorise = []

    for i in pseudo:
        if i not in liste_caractere_autorise:
            liste_caractere_non_autorise.append(i)

    if len(liste_caractere_non_autorise) == 0:
        return True

    else :
        print("Les caractères",liste_caractere_non_autorise,"ne sont pas autorisés")
        return False

def verif_taille_pseudo(pseudo,taille_minim,taille_max):

    if len(pseudo) >= taille_minim and len(pseudo) <= taille_max:
        return True
    else:
        
        return False