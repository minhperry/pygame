import random as r
import math

maxhp = 500
class player:

    def __init__(self, name):
        self.health = maxhp
        self.name = name

    # def display(self):
    #     print(f'Current HP: {self.health}')

    def heal(self):
        self.health += 15
        if self.health > maxhp:
            self.health = maxhp
    
    def randchance(chance):
        x = r.randint(1,100)
        if x <= chance: return True
        else: return False

    def attack(self, enemy):
        dmg = r.randint(11,20)
        enemy.health -= dmg
        return dmg

    def drain(self, enemy):
        tmphp = enemy.health
        if player.randchance(30) == True:
            enemy.health = round(enemy.health * 0.8)
        return (tmphp - enemy.health) 

    def critical(self, enemy):
        dmg = r.randint(10,25)
        self.health -= dmg
        enemy.health -= (2 * dmg)
        return dmg

    def kill(self, enemy):
        dmg = r.randint(15,35)
        self.health -= dmg
        enemy.health -= dmg
        return dmg