

class Player:
    def __init__(self):
        self.xp = 0
        self.xp_to_lvl_up = 100
        self.level = 1
        self.money = 0
        self.health = 200
        self.max_health = 200
        self.attack = 0
        self.max_attack = 0
        self.speed = 0

    def level_up(self):
        if self.level == 20:
            return
        
        self.xp-= self.xp_to_lvl_up
        self.xp_to_lvl_up += 25
        self.max_health += 25
        self.health = self.max_health
        self.attack += 5
        self.max_attack += 5
        self.speed += 1
        self.level += 1
        print (f"Level up !  Vous avez atteint le niveau {self.level} !" )