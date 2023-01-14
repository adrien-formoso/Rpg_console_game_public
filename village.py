import os
import random
from dictionaries import *




import random


def buy_item(item_type, items, inventory, money):
  #nombre rond pour acheter mais pas nécessaire
   
    #vérifie si l'objet est en stock ou non
    item = items.get(item_type)
    if not item:
        print(f"Je m'excuse, mais nous n'avons plus {item_type} en stock.")
        return money
    stock = item.get("stock", 0)
    if stock <= 0:
        print(f"Je m'excuse, mais nous n'avons plus {item['name']} en stock.")
        return money
    price = item.get("price", 0)
    if player.money < price:
        print(f"Vous n'avez pas assez d'argent pour effectué cet achat. Le prix est de : {price} et vous possédez : {player.money} golds.")
        return money
    inventory[item_type] = item
    item["stock"] = stock -1
    player.money -= price
    print(f"Vous avez acheté {item['name']} et dépensé {price}. Il vous reste {player.money} golds.")
    return money
    



def display_inventory(inventory):

    if not inventory:
        print("Votre inventaire est vide.")
        return
    print("Votre inventaire:")
    for item_type, item_info in inventory.items():
        print(f"{item_info['name']} (Price: {item_info.get('price',0)})")
        for key, value in item_info.items():
            if key != "name" and key != "price":
                print(f"\t{key}: {value}")
    print(f"Vous possédez : {player.money}.")



    buy_item('sword', items, inventory)
    display_inventory(inventory)

character = {"name": "John", "money": 50, "inventory": {}}
character["money"] = buy_item("potion1", items, character["inventory"], character["money"])

print(character)







def choose_side_quest(side_quests):
  if current_quest == None:

    # Choisir une quête au hasard
    quest_name = random.choice(list(side_quests.keys()))
    quest_info = side_quests[quest_name]

    print(f"Voici la quête qui vous a été attribué: {quest_name}")
    print(f"Difficulté: {quest_info['difficulté']}")
    print(f"Récompense: {quest_info['reward']} pièces d'or")
    print(f"Tâche à accomplir: {quest_info['But']}")

  elif current_quest != None:
    print("\n Finissez la quête en cours avant d'en débuter une nouvelle.")

    




side_quests = {
     "plus de rats" : {
         "difficulté" : "facile",
         "reward" : 50,
         "But" : "Rapporter 3 queues de rat"
     },
     "tueur de loups" : {
         "difficulté" : "moyenne",
         "reward" : 200,
         "But" : "Rapporter 2 peaux de loup"
     },
     "joffrey le fou pepouz" : {
         "difficulté" : "dur",
         "reward" : 800,
         "But" : "Rapporter un artefact du donjon" # retrouver les 5 morceaux de la dignité de joffrey
     },
     "Slay the dragon": {
         "difficulté": "ptdr force à toi afou",
         "reward": 100,
         "But": "Bring the dragon's head as proof of your victory"
     },
     "explorateur": {
         "difficulté" : "bonne chance frero",
         "reward" : "450",
         "But" : "Visiter tous les donjons"
     }
 }

choose_side_quest(side_quests)