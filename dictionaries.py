start_weapon = {
    "épée": {"name":"épée","attack":10},
    "baton magique": {"name":"baton magique","attack":10},
    "arc courbé": {"name":"arc courbé","attack":10}
}

monsters = {
    "loup":{"health":100,"attack":30, "speed":8, "xp": 80, 
        "loots":{"canine" : 5, "peau de loup":20}},

    "ours":{"health":300, "attack":50, "speed": 5, "xp":80,
        "loots":{"pâte d'ours": 5,"fourure d'ours" : 30}},

    "sanglier":{"health":130, "attack":35, "speed": 7, "xp":80,
        "loots":{"défense brisée":5,"peau de sanglier":20}},

    "rat":{"health":80, "attack":20, "speed": 10,"xp":80,
        "loots":{"griffe de rat":5,"queue de rat":15}},

    "araignée": {"health":150, "attack":40, "speed": 8, "xp":80,
        "loots":{"pâte d'araignée":5,"soie":20}},

    "bandit": {"health":250, "attack":45, "speed": 12, "xp":80,
        "loots":{"foulard":5,"dague brisée":20}},
}

boss_monsters= {
    "gnome": {"health":500,"attack":70,"speed":15,"xp":120,
              "loots":{"potion de soin supérieure","potion de force"}},
    "troll": {"health":750,"attack":95,"speed":17,"xp":150,
              "loots":{"potion de mana supérieure","potion d'énergie supérieure"}},
    "orc":   {"heatlh":1000,"attack":125,"speed":20,"xp":200},
    "le magicien noir":  {"health":1500,"attack":150, "speed":20,"xp":2000}
}



items = {
    "weapon1": {"name": "épée améliorée","attack": 30,"price": 5, "stock": 1},
    "weapon2": {"name": "baton magique amélioré","attack": 30,"price": 1, "stock":1},
    "weapon3": {"name": "arc courbé amélioré","attack": 30,"price": 1, "stock" : 1},
    "potion1": {"name": "potion de soin mineure","healing": 50,"price": 15, "stock": 5},
    "potion2": {"name": "potion de soin majeure","healing": 150,"price": 40, "stock": 5},
    "potion3": {"name": "potion de force mineure","healing": 10,"price": 30, "stock": 5},
    "potion4": {"name": "potion de force majeure","healing": 30,"price": 70, "stock": 5},
    "potion5": {"name": "potion de mana mineure","healing": 20,"price": 20, "stock": 5},
    "potion6": {"name": "potion de mana majeure","healing": 50,"price": 50, "stock": 5},
    "potion7": {"name": "potion d'énergie mineure","healing": 20,"price": 20, "stock": 5},
    "potion8": {"name": "potion d'énergie majeure","healing": 50,"price": 500, "stock": 5}
}

player.inventory.append("potion d'énergie majeure")
