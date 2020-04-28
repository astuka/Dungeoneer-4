import random as r

#creates a Character
class Character:
    def __init__(self,health=100,atk=10,de=10):
        self.health = health
        self.atk = atk
        self.de = de

#creates a Monster
class Monster:
    def __init__(self,name, health,atk,de):
        self.name = name
        self.health = health
        self.atk = atk
        self.de = de

#main menu
test = input("Welcome to Dungeoneer 4\n1. Start game \n")

#monster initialization
goblin = Monster("Goblin", 10, 13, 3)
orc = Monster("Orc", 5, 15, 5)
ogre = Monster("Ogre", 20, 11, 1)
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
                    print("You killed the "+monster.name)
                    fight = False
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