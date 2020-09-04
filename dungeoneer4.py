#TO DO
#the first enemy you fight in a zone is an enemy from the old zone, then it goes to the new zone. why? 
#incorporate elements from DnD
#add loot to enemies

import random as r
import content as c

monsters = c.lake_monsters

################################# FUNCTIONS #################################

#main menu
test = input("Welcome to Dungeoneer 4\n1. Start game \n2. Load Game\n")

#new game
if test == "1":
  player = c.Character()
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
    inventory = save.readline() #take in mind, grabbing an array here 
    player = c.Character(health,atk,de,mag,gold,xp,xp_cap,lvl, inventory)
    player_default = player.health

def switch_zone():
    print("\n")
    num_zone = 1
    for zone in c.zones:
        print(str(num_zone) +". "+ zone+"\n")
        num_zone += 1
    zone_choice = input("Which zone would you like to go to?\n")
    print(c.zones[int(zone_choice) - 1])
    if zone_choice == '1':
        ans0 = input("You are in town. What would you like to do?\n1.Buy/Sell items\n2.Get a Quest\n3.Switch Zones")
        if ans0 == '1':
            shop = c.items #for now, change when there's multiple town zones
            ans1 = input("Would you like to buy or sell?")
            if ans1 == "Buy": 
                n = 0
                print("Shop's Inventory:\n")
                for item in shop:
                    print(str(n)+". "+shop[n].name +", "+str(shop[n].buy_price))
                    n += 1
                #input: what item would you like to buy?
                #if money > buy, take money out and put item in inventory
                #print you have bought X

            elif ans1 == "Sell":
                n = 1
                print("Player's Inventory:\n")
                for item in player.inventory:
                    print(str(n)+". "+player.inventory[item].name +", "+str(player.inventory[item].sell_price))
                    n+=1 
                #input: what item would you like to sell?
                    #money + sell price, remove from inventory
                    #print you have sold X

        if ans0 == '2':
            print("Available Quests:\n")
            n = 0
            for quest in c.quests:
                print(str(n)+". "+c.quests[n].name+": "+c.quests[n].text)
                n += 1
            #get quest
                #get list of quests
                #user can choose one, added to their quest list
                #when they hit the goal, automatically get rewards 
        if ans0 == '3':
            switch_zone()
    if zone_choice == '2':
        monsters = c.lake_monsters   
    if zone_choice == '3':
        monsters = c.forest_monsters

################################# GAME LOOP #################################

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
                for skill in c.skills:
                    print(str(num_skill) +". "+ skill.name+"\n")
                    num_skill += 1
                skill_choice = input("Which skill would you like to use?\n")
                print(c.skills[int(skill_choice) - 1])
                if skill_choice == '1':
                    played_skill = c.fireball     
                if player.mag >= played_skill.cost:
                    player.mag -= played_skill.cost
                    if played_skill.typ == c.magic_attack:
                         monster.health -= played_skill.ability 
                         player.health -= max(r.randrange(0,monster.atk) - r.randrange(0,player.de),0)
                    elif played_skill.typ == c.magic_defense:
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
            switch_zone()
        if ans0 == "3":
            save = open('save.txt','w')
            n = [str(player.health)+"\n", str(player.atk)+"\n", str(player.de)+"\n",str(player.mag)+"\n", str(player.xp)+"\n",str(player.xp_cap)+"\n", str(player.lvl)+"\n"]
            save.writelines(n)
            save.close()
            print("Player saved.\n")

else:
    while test != "1":
        test = input("Please choose a valid option.\n")