################################# CLASSES #################################


#creates a Character
class Character:
    def __init__(self,health=100,atk=10,de=10, mag=10, gold=0, xp=0, xp_cap = 100, lvl = 1, inventory=[]):
        self.health = health
        self.atk = atk
        self.de = de
        self.mag = mag
        self.gold = gold
        self.xp = xp
        self.xp_cap = xp_cap
        self.lvl = lvl
        self.inventory = inventory

#creates a Monster
class Monster:
    def __init__(self,name, health,atk,de, xp):
        self.name = name
        self.health = health
        self.atk = atk
        self.de = de
        self.xp = xp

#creates a Skill
class Skill:
    def __init__(self, name, typ, ability, cost):
        self.name = name
        self.typ = typ
        self.ability = ability
        self.cost = cost

#creates an Item
class Item:
    def __init__(self, name, typ, ability, sell_price, buy_price):
        self.name = name
        self.typ = typ #armor, weapon, consumable
        self.ability = ability #effects different parts depending on typ
        self.sell_price = sell_price
        self.buy_price = buy_price
#if equip, adds to stats until un equiped (some function decides this)
#if consum, one time use

#creates a Class
class Class:
    def __init__(self,name, skills, health, atk, de,mag):
        self.name = name
        self.skills = skills #an array that replaces skills down below
        self.health = health #added/subtracted from base
        self.atk = atk #added/subtracted from base
        self.de = de #added/subtracted from base
        self.mag = mag #added/subtracted from base
#have person choose from array at beginning of new game

#creates a Quest
class Quest:
    def __init__(self,name,text,current,goal,reward,reward_type):
        self.name = name #name of quest on list
        self.text = text #expanded quest description
        self.current = current #current scenario
        self.goal = goal #goal scenario
        self.reward = reward #amount or name of item
        self.reward_type = reward_type #gold, xp, etc.



################################# ASSETS #################################


#skill types
magic_attack = 0
magic_defense = 1

#skill initialization
fireball = Skill("Fireball", magic_attack, 10, 10)
slash = Skill("Slash", magic_attack, 10, 10)
gigaslash = Skill("GigaSlash", magic_attack, 25, 20)

skills = [fireball, slash, gigaslash]

#item types
weapon = 0
armor = 1
accessory = 2
potion = 3

#item initialization
iron_sword = Item("Iron Sword", weapon, 2, 5, 10)

items = [iron_sword]

#class initialization
warrior = Class("Warrior",[slash,gigaslash],0, 5, 0, -5 ) #add the skills to skill init

classes = [warrior]

#reward types
gold = 0
xp = 1
item = 2

#quest initialization
goblin_5 = Quest("Kill 5 Goblins", "Kill 5 goblins to complete this quest", 0, 5, 100,0)

quests = [goblin_5]

#monster initialization
goblin = Monster("Goblin", 10, 13, 3, 10)
orc = Monster("Orc", 5, 15, 5, 15)
ogre = Monster("Ogre", 20, 11, 1, 20)

sahuagin = Monster("Sahuagin", 5, 15, 1, 20)
naga = Monster("Naga", 15, 5, 1, 20)


#zones + monsters
zones = ["Town","Lake [Levels 1-2]", "Forest [Levels 2-3]"]
lake_monsters = [sahuagin, naga]
forest_monsters = [goblin, orc, ogre]
