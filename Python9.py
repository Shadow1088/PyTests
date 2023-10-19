import math
import random

player_level = 1
world_level = math.ceil(player_level/10)
time = 1
in_sight = True
exists = True

print(world_level)

dmg_bonuses = {"a":10,"b":20,"c":30,"d":40,"e":50,"f":60,"g":70,"h":80}
armor_bonuses = {}
hp_bonuses = {}

dmg_bonuses_values = sum(dmg_bonuses.values())
armor_bonuses_values = sum(armor_bonuses.values())
hp_bonuses_values = sum(hp_bonuses.values())

player_hp = 100 + hp_bonuses_values + (world_level*3)
player_dmg = 10 + dmg_bonuses_values
player_armor = 0 + armor_bonuses_values

if player_hp <= 0:
    print("You lose")

    
game_inventory = {

    "Blue Talisman(armor)": 200,
    "Shadowed Cloak(armor)": 20,
    "Spiky gloves(damage)": 30,
    "Fish1(health)": 20,
    "Fish2(health)": 30,
    "Fish3(health)": 50,
    "Fish4(health)": 65,
    "HSpell1(health)": 70,
    "HSpell2(health)": 80,
    "HSpell3(health)": 100,


}


pr_len_dmg_b = len(dmg_bonuses)
pr_len_armor_b = len(armor_bonuses)
pr_len_health_b = len(hp_bonuses)

dmg_bonuses["i"] = 9

# while pr_len_dmg_b < len(dmg_bonuses):
#     if len(dmg_bonuses) > pr_len_dmg_b:
#         print(dmg_bonuses[len(dmg_bonuses)-2])
#         pr_len_dmg_b = len(dmg_bonuses)
#         print("working")
#         print(len(dmg_bonuses))




class Armor_box:
    def __init__(self):
        self.blue_talisman = 200
        self.shadowed_cloak = 20
        self.spiky_gloves = 30

armor_box = Armor_box()


class Monster:

    # attributes
    health = int(100*(world_level/5))
    energy = 60
    speed = 20
    ##

    def __init__(self, health, energy, speed):
        self.health = health
        self.energy = energy
        self.speed = speed

    def __str__(self):
        return f"Monster: health = {self.health}, energy = {self.energy}, speed = {self.speed}"
    
    ##

    # methods
    def attack(self,damage):
        print(f"{monster}: attack ({damage} damage dealt)")
    
    def defend(self,blocked):
        num = random.randrange(0,3)
        if num == 2:
            print(f"{monster}: defend ({blocked} damage was blocked)")
    
    def move(self, speed):
        tups = int(speed/2*(time))
        print(f"{monster}: move ({tups} tups)")



monster_common = Monster(int(100*(world_level/5)),60,20)
#
monster = "monster_common"
#
monster_common.attack(int(world_level*1.5))
monster_common.defend(int(world_level*0.5))
monster_common.move(20)


monster_rare = Monster(int(100*(world_level/5)),60,20)    
monster = "monster_rare"
monster_rare.move(20+10)
monster_rare.attack(int(world_level*1.5+10))


monster_epic = Monster(int(100*(world_level/5)),60,20)
monster = "monster_epic"
monster_epic.attack(int(world_level*2+30))
monster_epic.defend(int(world_level*0.5+30))



monster_legendary = Monster(int(100*(world_level/5)),60,20)
monster = "monster_legendary"
monster_legendary.attack(int(world_level*2.5+50))
monster_legendary.defend(int(world_level*0.5+50))



Armor_box_dict = {"Blue Talisman":200, "Shadowed Cloak":20, "Spiky gloves":30}
Armor_box_poss = random.choice(list(Armor_box_dict.items()))

def Armor_box_obtained():
    print (f"Armor box obtained, you have received {Armor_box_poss[0]}")
    print (f"Added {Armor_box_poss[1]} armor")
    armor_bonuses[Armor_box_poss[0]] = Armor_box_poss[1]

Armor_box_obtained()






























print(f"Player damage: {player_dmg}")
print(f"player_hp: {player_hp}")
print(f"player_armor: {player_armor}")

def stats_reset():
    player_hp = 100 + hp_bonuses_values + (world_level*3)
    player_dmg = 10 + dmg_bonuses_values
    player_armor = 0 + armor_bonuses_values

    hp_bonuses.clear()
    dmg_bonuses.clear()
    armor_bonuses.clear()

    world_level = 1
    player_level = 1

    print(f"player_hp: {player_hp}")
    print(f"player_dmg: {player_dmg}")
    print(f"player_armor: {player_armor}")
    print(f"player_level: {player_level}")
