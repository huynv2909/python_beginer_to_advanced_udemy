from classes.game import Person, bcolors
from classes.Magic import Spell
from classes.inventory import Item
import random

# Create black magics
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 12, 120, "black")

# Create white magics
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super potion", "potion", "Heals 500 HP", 500)

elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one part member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restore party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# prepare properties
player_magics = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},
                {"item": grenade, "quantity": 5}]

player1 = Person("John", 460, 65, 50, 40, player_magics, player_items)
player2 = Person("Dany", 570, 75, 55, 50, player_magics, player_items)
player3 = Person("Alex", 855, 90, 80, 90, player_magics, player_items)
enemy = Person("Enemy", 2000, 65, 200, 300, [], [])

players = [player1, player2, player3]

running = True

print("\n" + bcolors.WARNING + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("****************************\n")
    print("NAME\t\t\t\t\tHP\t\t\t\t\t\t\t\t\t\tMP")
    for player in players:
        player.get_stats()

    print("------------")
    print("Enemy:")
    enemy.get_stats()

    for player in players:
        if player.hp > 0:
            player.choose_action()
            choice = input("Choose action: ")
            index = int(choice) - 1
            if index == 0:
                dmg = player.generate_damage()
                enemy.take_damage(dmg)
                print(player.name + " attacked for", dmg, "points of damage")
            elif index == 1:
                player.choose_magic()
                magic_choice = int(input("Choose magic:")) - 1

                if magic_choice == -1:
                    continue

                spell = player.magic[magic_choice]
                magic_dmg = spell.generate_damage()

                current_mp = player.get_mp()

                if spell.cost > current_mp:
                    print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                    continue

                player.reduce_mp(spell.cost)

                if spell.type == "white":
                    player.heal(magic_dmg)
                    print(bcolors.OKBLUE + "\n" + spell.name + " heals", str(magic_dmg), "HP" + bcolors.ENDC)
                elif spell.type == "black":
                    enemy.take_damage(magic_dmg)
                    print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
            elif index == 2:
                player.choose_item()
                item_choice = int(input("Choose item:")) - 1

                if item_choice == -1:
                    continue

                if player.items[item_choice]["quantity"] == 0:
                    print(bcolors.FAIL + "\nOut of item" + bcolors.ENDC)
                    continue
                else:
                    player.items[item_choice]["quantity"] -= 1

                item = player.items[item_choice]["item"]

                if item.type == "potion":
                    player.heal(item.prop)
                    print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
                elif item.type == "elixer":
                    if item.name == "MegaElixer":
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name + " fully restore HP/MP" + bcolors.ENDC)
                elif item.type == "attack":
                    enemy.take_damage(item.prop)
                    print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)
            print("----------------------")

    # Enemy turn
    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    target_list = []
    for i in range(0, len(players)):
        if players[i].hp > 0:
            target_list.append(i)

    target_enemy = random.choice(target_list)
    players[target_enemy].take_damage(enemy_dmg)
    print("Enemy attacked " + players[target_enemy].name + " for", enemy_dmg)
    print("--------------------------------")

    survivals_list = []
    for i in range(0, len(players)):
        if players[i].hp > 0:
            survivals_list.append(i)

    if len(survivals_list) == 0:
        print(bcolors.FAIL + "Enemy has defeated you!" + bcolors.ENDC)
        running = False
    else:
        if enemy.get_hp() == 0:
            print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
            running = False


