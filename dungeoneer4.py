#TO DO
#the first enemy you fight in a zone is an enemy from the old zone, then it goes to the new zone. why? 
#incorporate elements from DnD

import random as r

#creates a Character
class Character:
    def __init__(self,health=100,atk=10,de=10, mag=10, gold=0, xp=0, xp_cap = 100, lvl = 1):
        self.health = health
        self.atk = atk
        self.de = de
        self.mag = mag
        self.gold = gold
        self.xp = xp
        self.xp_cap = xp_cap
        self.lvl = lvl

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






#main menu
test = input("Welcome to Dungeoneer 4\n1. Start game \n2. Load Game\n")

#skill types
magic_attack = 0
magic_defense = 1

#skill initialization
fireball = Skill("Fireball", magic_attack, 10, 10)

skills = [fireball]

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

monsters = lake_monsters

#new game
if test == "1":
  player = Character()
  player_default = player.health

#load game
if test == "2":
    #set a thing if they try to open this and there's no save theres an error
    save = open('save.txt','r')
    #convert this to a for loop next time
    health = int(save.readline())
    atk = int(save.readline())
    de = int(save.readline())
    mag = int(save.readline())
    gold = int(save.readline())
    xp = int(save.readline())
    xp_cap = int(save.readline())
    lvl =int(save.readline())
    player = Character(health,atk,de,mag,gold,xp,xp_cap,lvl)
    player_default = player.health


#game loop
game = True
while game:
    #pick monster
    monster = monsters[r.randrange(0,len(monsters))]
    #make sure monsters health doesnt save
    monster_default = monster.health
    fight = True
    while fight: 
        ans0 = input("You are fighting a "+monster.name+". What would you like to do?\n1.Attack\n2.Switch Zone\n3.Save\n")
        if ans0 == "1":
            ans1 = input("What type of attack?\n1.Normal\n2.Magic\n")
            if ans1 == "1":
                monster.health -= max(r.randrange(0,player.atk) - r.randrange(0,monster.de),0) #either does damage or blocks all damage
                player.health -= max(r.randrange(0,monster.atk) - r.randrange(0,player.de),0) #set this so that there's higher base than 0
            if ans1 == "2":
                print("\n")
                num_skill = 1
                for skill in skills:
                    print(str(num_skill) +". "+ skill.name+"\n")
                    num_skill += 1
                skill_choice = input("Which skill would you like to use?\n")
                print(skills[int(skill_choice) - 1])
                if skill_choice == '1':
                    played_skill = fireball     
                if player.mag >= played_skill.cost:
                    player.mag -= played_skill.cost
                    if played_skill.typ == magic_attack:
                         monster.health -= played_skill.ability 
                         player.health -= max(r.randrange(0,monster.atk) - r.randrange(0,player.de),0)
                    elif played_skill.typ == magic_defense:
                        player.health -= max(r.randrange(0,monster.atk) - r.randrange(0,player.de) - played_skill.ability,0)
                else:
                    print("You did not have enough magic for that spell, and whiffed!")
                    player.health -= max(r.randrange(0,monster.atk) - r.randrange(0,player.de),0)

            if monster.health <= 0:
                print("You killed the "+monster.name+" and received "+str(monster.xp)+" XP.")
                fight = False
                player.xp += monster.xp
                if player.xp >= player.xp_cap:
                    player.lvl += 1
                    player.xp = 0
                    player.health = player_default + 10
                    player_default = player.health 
                    player.atk += 1
                    player.de += 1
                    player.mag += 5
                    player.xp_cap += 50
                    print("You leveled up! You are now level "+str(player.lvl))
                #reset monster health
                monster.health = monster_default
            else:
                print(monster.name+" is now at "+str(monster.health)+". You are now at "+str(player.health)+"\n")
            if player.health <= 0:
                print("You died.")
                fight = False
                game = False
        if ans0 == "2":
            print("\n")
            num_zone = 1
            for zone in zones:
                print(str(num_zone) +". "+ zone+"\n")
                num_zone += 1
            zone_choice = input("Which zone would you like to go to?\n")
            print(zones[int(zone_choice) - 1])
            if zone_choice == '1':
                #new menu items: buy/sell, get quest, switch zones
                #buy/sell: get list of items from shop, get list of items on character
                    #find item value, compare that with character money if buying
                    #check if character has it if selling
                #get quest
                    #get list of quests
                    #user can choose one, added to their quest list
                    #when they hit the goal, automatically get rewards 
            if zone_choice == '2':
                monsters = lake_monsters   
            if zone_choice == '3':
                monsters = forest_monsters
        if ans0 == "3":
            save = open('save.txt','w')
            n = [str(player.health)+"\n", str(player.atk)+"\n", str(player.de)+"\n",str(player.mag)+"\n", str(player.xp)+"\n",str(player.xp_cap)+"\n", str(player.lvl)+"\n"]
            save.writelines(n)
            save.close()
            print("Player saved.\n")

else:
    while test != "1":
        test = input("Please choose a valid option.\n")