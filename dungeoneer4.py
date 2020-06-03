#TO DO
#the first enemy you fight in a zone is an enemy from the old zone, then it goes to the new zone. why? 
#incorporate elements from DnD
#add magic/skills
#add items
#recommended levels for the zones
#add classes

import random as r
#import numpy as np

#creates a Character
class Character:
    def __init__(self,health=100,atk=10,de=10, mag=10, xp=0, xp_cap = 100, lvl = 1):
        self.health = health
        self.atk = atk
        self.de = de
        self.mag = mag
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

class Skill:
    def __init__(self, name, typ, ability, cost):
        self.name = name
        self.typ = typ
        self.ability = ability
        self.cost = cost


#main menu
test = input("Welcome to Dungeoneer 4\n1. Start game \n2. Load Game\n")

#monster initialization
goblin = Monster("Goblin", 10, 13, 3, 10)
orc = Monster("Orc", 5, 15, 5, 15)
ogre = Monster("Ogre", 20, 11, 1, 20)

sahuagin = Monster("Sahuagin", 5, 15, 1, 20)
naga = Monster("Naga", 15, 5, 1, 20)


#zones + monsters
zones = ["Lake", "Forest"]
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
    xp = int(save.readline())
    xp_cap = int(save.readline())
    lvl =int(save.readline())
    player = Character(health,atk,de,mag,xp,xp_cap,lvl)
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
        ans = input("You are fighting a "+monster.name+". What would you like to do?\n1.Attack\n2.Switch Zone\n3.Save\n")
        if ans == "1":
            monster.health -= max(r.randrange(0,player.atk) - r.randrange(0,monster.de),0) #either does damage or blocks all damage
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
        if ans == "2":
            print("\n")
            num_zone = 1
            for zone in zones:
                print(str(num_zone) +". "+ zone+"\n")
                num_zone += 1
            zone_choice = input("Which zone would you like to go to?\n")
            print(zones[int(zone_choice) - 1])
            if zone_choice == '1':
                monsters = lake_monsters    
            if zone_choice == '2':
                monsters = forest_monsters   
        if ans == "3":
            save = open('save.txt','w')
            n = [str(player.health)+"\n", str(player.atk)+"\n", str(player.de)+"\n",str(player.mag)+"\n", str(player.xp)+"\n",str(player.xp_cap)+"\n", str(player.lvl)+"\n"]
            save.writelines(n)
            save.close()
            print("Player saved.\n")

else:
    while test != "1":
        test = input("Please choose a valid option.\n")