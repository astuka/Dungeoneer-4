import random as r

class Character:
    def __init__(self,health=100,atk=10,de=10):
        self.health = health
        self.atk = atk
        self.de = de

class Monster:
    def __init__(self,name, health,atk,de):
        self.name = name
        self.health = health
        self.atk = atk
        self.de = de

test = input("Welcome to Dungeoneer 4\n1. Start game \n")

goblin = Monster("Goblin", 10, 3, 3)
orc = Monster("Orc", 5, 5, 5)
ogre = Monster("Ogre", 20, 1, 1)

monsters = [goblin,orc,ogre]

game = True

if test == "1":
    player = Character()
    while game:
        monster = monsters[r.randrange(0,len(monsters))]
        fight = True
        while fight: 
            ans = input("You are fighting a "+monster.name+". What would you like to do?\n1.Attack\n")
            if ans == "1":
                monster.health -= player.atk
                player.health -= monster.atk
                if monster.health <= 0:
                    print("You killed the "+monster.name)
                    fight = False
                if player.health <= 0:
                    print("You died.")
                    fight = False
                    game = False
                print(monster.name+" is now at "+str(monster.health)+". You are now at "+str(player.health)+"\n")
else:
    while test != "1":
        test = input("Please choose a valid option.\n")