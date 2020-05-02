#TO DO
# Make xp_cap expand over time
# make lvl actually do things for player


import random as r

#creates a Character
class Character:
    def __init__(self,health=100,atk=10,de=10, xp=0, xp_cap = 100, lvl = 1):
        self.health = health
        self.atk = atk
        self.de = de
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

#main menu
test = input("Welcome to Dungeoneer 4\n1. Start game \n")

#monster initialization
goblin = Monster("Goblin", 10, 13, 3, 10)
orc = Monster("Orc", 5, 15, 5, 15)
ogre = Monster("Ogre", 20, 11, 1, 20)
monsters = [goblin,orc,ogre]

#game loop
game = True
if test == "1":
    player = Character()
    while game:
        #pick monster
        monster = monsters[r.randrange(0,len(monsters))]
        #make sure monsters health doesnt save
        monster_default = monster.health
        fight = True
        while fight: 
            ans = input("You are fighting a "+monster.name+". What would you like to do?\n1.Attack\n")
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
                        player.health = 100 #this is a hardcode, needs to be fixed
                        #add xp_cap scaling here
                        print("You leveled up! You are now level "+str(player.lvl))
                    #reset monster health
                    monster.health = monster_default
                else:
                    print(monster.name+" is now at "+str(monster.health)+". You are now at "+str(player.health)+"\n")
                if player.health <= 0:
                    print("You died.")
                    fight = False
                    game = False
else:
    while test != "1":
        test = input("Please choose a valid option.\n")