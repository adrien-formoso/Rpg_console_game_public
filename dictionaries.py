start_weapon = {
    "épée": {"name":"épée","attack":10},                            #dictionnaire des armes pour débuter 
    "baton magique": {"name":"baton magique","attack":10},
    "arc courbé": {"name":"arc courbé","attack":10}
}

end_weapon = {
    "épée": {"name":"épée de la garde royale","attack":70},                            #dictionnaire des armes trouvés dans le coffre de fin
    "baton": {"name":"baton des milles-tempêtes","attack":70},
    "arc": {"name":"arc long des gardiens anciens","attack":70}
}



monsters = {
    "loup":{"health":100,"attack":25, "speed":8, "xp": 80,          #dictionnaire des monstres de la forêt qui apparaissent aléatoirement
        "loots":{"canine" : 5, "peau de loup":20}},                 #l'xp est mis à 80 pour éviter de devoir passer trop de temps sur le jeu lors du test

    "ours":{"health":300, "attack":40, "speed": 5, "xp":80,
        "loots":{"patte d'ours": 5,"fourure d'ours" : 30}},

    "sanglier":{"health":130, "attack":30, "speed": 7, "xp":80,
        "loots":{"défense brisée":5,"peau de sanglier":20}},

    "rat":{"health":80, "attack":15, "speed": 10,"xp":80,
        "loots":{"griffe de rat":5,"queue de rat":15}},

    "araignée": {"health":150, "attack":35, "speed": 8, "xp":80,
        "loots":{"patte d'araignée":5,"soie":20}},

    "bandit corrompu": {"health":250, "attack":40, "speed": 12, "xp":80,
        "loots":{"foulard":5,"dague brisée":20}},

    "sorcier corrompu": {"health":230, "attack":35, "speed": 12, "xp":80,
        "loots":{"foulard":5,"bâton brisé":20}},

    "wyrm": {"health":150, "attack":20, "speed": 15, "xp":80,
        "loots":{"écaille":5,"dent de wyrm":20}},

    "gnoll": {"health":270, "attack":40, "speed": 14, "xp":80,
        "loots":{"patte de gnoll":5,"oreille de gnoll":20}},
}

boss_monsters= {                                                     #dictionnaire des monstres du donjon 
    "gnome": {"health":350,"attack":50,"speed":15,"xp":120,
              "loots":{}},
    "troll": {"health":400,"attack":65,"speed":17,"xp":150,
              "loots":{}},
    "orc":   {"health":630,"attack":80,"speed":20,"xp":200,
            "loots":{}},
    "mage_noir":  {"health":4000,"attack":300, "speed":30,"xp":2000,
                "loots":{}},
    "nerathor": {"health":4000,"attack":300, "speed":30,"xp":2000,
                "loots":{}}
}



items = {                                                           #dictionnaire des objets du shop
    "weapon1": {"name": "épée améliorée","type": "Guerrier", "attack": 30,"price": 50, "stock": 1},
    "weapon2": {"name": "baton magique amélioré","type": "Mage","attack": 30,"price": 50, "stock":1},
    "weapon3": {"name": "arc courbé amélioré","type": "Chasseur","attack": 30,"price": 50, "stock" : 1},
    "potion1": {"name": "potion de soin mineure","healing": 50,"price": 20, "stock": 5},
    "potion2": {"name": "potion de soin majeure","healing": 150,"price": 60, "stock": 5},
    "potion3": {"name": "potion de force mineure","healing": 10,"price": 30, "stock": 5},
    "potion4": {"name": "potion de force majeure","healing": 30,"price": 50, "stock": 5},
    "potion5": {"name": "potion de mana mineure","healing": 20,"price": 20, "stock": 5},
    "potion6": {"name": "potion de mana majeure","healing": 50,"price": 40, "stock": 5},
    "potion7": {"name": "potion d'énergie mineure","healing": 20,"price": 20, "stock": 5},
    "potion8": {"name": "potion d'énergie majeure","healing": 50,"price": 40, "stock": 5}
}



global_loot = {                       #dictionaire des objets vendables
    "canine" : 5, 
    "peau de loup":20,
    "patte d'ours": 5,
    "fourure d'ours" : 30,
    "défense brisée":5,
    "peau de sanglier":20,
    "griffe de rat":5,
    "queue de rat":15,
    "patte d'araignée":5,
    "soie":20,
    "foulard":5,
    "dague brisée":20,
    "écaille":5,
    "dent de wyrm":20,
    "patte de gnoll":5,
    "oreille de gnoll":20,
    "bâton brisé":20,
    "baton magique amélioré":50,
    "arc courbé amélioré":50,
    "épée amélioré":50,
    "épée":10,
    "baton magique":10,
    "arc courbé":10
}
