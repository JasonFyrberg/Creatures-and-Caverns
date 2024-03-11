import math
import random
import sys
from extras import *

#CLASSES HERE TO PREVENT CIRCULAR IMPORT
class Weapon:
    def __init__(self, name, base_damage, min_dmg_roll, max_dmg_roll):
        self.name = name
        self.base_damage = base_damage
        self.min_dmg_roll = min_dmg_roll
        self.max_dmg_roll = max_dmg_roll
wooden_club = Weapon("WOODEN CLUB", 2, 0, 3)
steel_flail = Weapon("STEEL FLAIL", 5, 0, 3)
greatsword = Weapon("GREATSWORD", 7, 0, 3) 
twin_daggers = Weapon('TWIN DAGGERS', 4, 0, 10)
brass_knuckles = Weapon('BRASS KNUCKLES', 8, 0, 4)
iron_hatchet = Weapon('IRON HATCHET', 9, 0 ,5)
warforged_hammer = Weapon("WARFORGED HAMMER", 11, 0, 4)
steamtech_gloves = Weapon("STEAMTECH GLOVES", 14, 0, 8)

class Armor:
    def __init__(self, name, value):
        self.name = name
        self.value = value
swim_trunks = Armor("SWIM TRUNKS", 50)
football_helmet = Armor('FOOTBALL HELMET', 30)
timbs = Armor('WORK BOOTS', 20)
vikings_helmet = Armor('VIKINGS HELMET', 15)
steel_chestpiece = Armor('STEEL BREASTPLATE', 30)
leather_pants = Armor('LEATHER PANTS', 10)
obsidian_gauntlets = Armor('OBSIDIAN GAUNTLETS', 25)


class Character:
    def __init__(self, name, weapon, curr_health, max_health, armor, accuracy, min_acc_roll, max_acc_roll):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.curr_health = curr_health
        self.max_health = max_health + armor.value
        self.accuracy = accuracy
        self.min_acc_roll = min_acc_roll
        self.max_acc_roll = max_acc_roll
    
class Monster:
    def __init__(self, name, health, base_damage, min_dmg_roll, max_dmg_roll, accuracy, min_acc_roll, max_acc_roll, run_chance, min_run, max_run):
        self.name = name
        self.health = health
        self.base_damage = base_damage 
        self.min_dmg_roll = min_dmg_roll
        self.max_dmg_roll = max_dmg_roll
        self.accuracy = accuracy
        self.min_acc_roll = min_acc_roll
        self.max_acc_roll = max_acc_roll
        self.run_chance = run_chance
        self.min_run = min_run
        self.max_run = max_run
slime1 = Monster("SLIME", 8, 3, 0, 1, 95, 0, 100, 0, 0 ,100)
normal_slime1 = Monster("SLIME", 8, 2, 0, 1, 95, 0, 100, 70, 0 ,100)
normal_slime2 = Monster("SLIME", 8, 2, 0, 1, 95, 0, 100, 70, 0 ,100)
bat1 = Monster("BAT", 7, 3, 0, 3, 85, 0, 100, 55, 0, 100)
bat2 = Monster("BAT", 7, 3, 0, 3, 85, 0, 100, 55, 0, 100)
bat3 = Monster("BAT", 7, 3, 0, 3, 85, 0, 100, 55, 0, 100)
bat4 = Monster("BAT", 7, 3, 0, 3, 85, 0, 100, 55, 0, 100)
troll = Monster("TROLL", 20, 8, 0, 5, 80, 0, 100, 65, 0, 100)
mimic = Monster("MIMIC", 35, 5, 0, 2, 90, 0, 100, 65, 0, 100)
mud_toad = Monster("MUD TOAD", 24, 4, 0, 3, 85, 0, 100, 0, 0, 100)
large_mud_toad = Monster("LARGE MUD TOAD", 36, 8, 0, 6, 90, 0, 100, 25, 0, 100)
hulkering_umbra = Monster("Hulkering Umbra", 55, 7, 0, 6, 80, 0, 100, 0, 0, 100)


#FUNCTIONS THAT TAKE IN CLASS DATA/USE OUTSIDE FUNCTIONS IN ORDER TO SIMULATE TURN BASED COMBAT
def mc_attack(self, enemy):
        damage = (self.weapon.base_damage + roll(self.weapon.min_dmg_roll, self.weapon.max_dmg_roll)) 
        enemy.health -= damage
        print(f"You did {damage} damage to the {enemy.name}!")

def enemy_attack(enemy, self):
    damage = (enemy.base_damage + roll(enemy.min_dmg_roll, enemy.max_dmg_roll))
    self.curr_health -= damage
    print(f"The {enemy.name} did {damage} damage to you!")

def combat(self, enemy):

    def combat_inventory():
        print("You can't access your inventory in the middle of combat, it's too dangerous!")
        separation()

    print(f"You are attacked by a {enemy.name}!")
    while self.curr_health > 0 and enemy.health > 0:
        separation()
        action = input("What do you want to do? (Attack/Run) ").strip().lower()

        if action == 'inventory':
            combat_inventory()

        elif action =='stats':
            check_stats()

        elif action == 'attack':
            mc_ac_check = roll(self.min_acc_roll, self.max_acc_roll)
            if  mc_ac_check < self.accuracy:
                mc_attack(self, enemy)
                if enemy.health <= 0:
                    break

            else: 
                print("Your attack missed!")

            enemy_ac_check = roll(enemy.min_acc_roll, enemy.max_acc_roll)
            if enemy_ac_check < enemy.accuracy:
                enemy_attack(enemy, self)

            else:
                print(f"{enemy.name}'s attack missed!")
                separation()  

        elif action == 'run':
            run_check = roll(enemy.min_run, enemy.max_run)
            if run_check < enemy.run_chance:
                print(f"You succesfully ran away from the {enemy.name}!")
                separation()
                break
            else:
                print("You couldn't run away!")
                enemy_ac_check = roll(enemy.min_acc_roll, enemy.max_acc_roll)
                if enemy_ac_check < enemy.accuracy:
                    enemy_attack(enemy, self)
                else:
                    print(f"{enemy.name}'s attack missed!")
                    separation()
        else:
            invalid_input()

    if self.curr_health <= 0:
        print(f"You have been defeated by the {enemy.name}")
        game_over()
    elif enemy.health <= 0:
        print(f"You have defeated the {enemy.name}")
        separation()

#PLAYERS INVENTORY THAT THEY CAN ACCESS AND USE ITEMS THEY GATHER
def health_potion():
    if main_character.curr_health == main_character.max_health:
        print("Your health is already full!")
    else:
        main_character.curr_health = main_character.max_health
        print("Your health has been restored to full!")
        print("You have used HEALTH POTION")
        separation()
        player_inventory.remove('HEALTH POTION')

def switch_weapons(other_weapon):
    print(f"You found a {other_weapon.name}!")
    weapon_dmg_mc()
    weapon_dmg_other(other_weapon)
    while True:
        new_weapon = input(f"Do you want to equip the {other_weapon.name}? (yes/no) ")
        if new_weapon == 'yes':
            player_inventory.remove(main_character.weapon.name)
            player_inventory.append(other_weapon.name)
            main_character.weapon = other_weapon
            print(f"You equipped the {other_weapon.name}!")
            separation()
            break
        elif new_weapon == 'no':
            print(f"You leave the {other_weapon.name} on the ground.")
            break
        else:
            invalid_input()

def update_armor(self, other_armor):
    self.curr_health = (self.curr_health + other_armor.value)
    self.max_health = self.max_health + other_armor.value
    self.armor = other_armor

def switch_armor(other_armor):
    print(f"You found a {other_armor.name}!")
    armor_val_mc()
    armor_val_other(other_armor)
    while True:
        new_armor = input(f"Do you want to equip the {other_armor.name}? (yes/no) ")
        if new_armor == 'yes':
            player_inventory.remove(main_character.armor.name)
            player_inventory.append(other_armor.name)
            
            print(f"You equipped the {other_armor.name}!")
            separation()
            update_armor(main_character, other_armor)
            break
        elif new_armor == 'no':
            print(f"You leave the {other_armor.name} on the ground.")
            break
        else:
            invalid_input()

def weapon_dmg_mc():
    print(f"Your {main_character.weapon.name} does {main_character.weapon.base_damage} damage + ({main_character.weapon.min_dmg_roll} to {main_character.weapon.max_dmg_roll}).")

def weapon_dmg_other(other_weapon):
    print(f"The {other_weapon.name} does {other_weapon.base_damage} damage + ({other_weapon.min_dmg_roll} to {other_weapon.max_dmg_roll}).")

def armor_val_mc():
    print(f"Your {main_character.armor.name} blocks {main_character.armor.value} damage.")

def armor_val_other(other_armor):
    print(f"The {other_armor.name} blocks {other_armor.value} damage.")

def access_inventory():
    print("Inventory: ")
    for item in player_inventory:
        print(item)
    while True:
        inventory_prompt = input("Which item would you like to use? ").strip().upper()
        separation()
        if inventory_prompt == 'EXIT':
            break
        if inventory_prompt == 'STATS':
            check_stats()
        elif inventory_prompt in player_inventory:
            if inventory_prompt == 'HEALTH POTION':
                health_potion()
            elif inventory_prompt == main_character.weapon.name:
                print(f"You swing your {main_character.weapon.name} but there are no enemies around.")
            elif inventory_prompt == main_character.armor.name:
                print(f"You look at the {main_character.armor.name}s you're wearing, how stylish!")
            else:
                print(f"You pull out and examine your {inventory_prompt}.")
        else:
            invalid_input()

def check_stats():
    print(f"Your current weapon is a {main_character.weapon.name}, it does {main_character.weapon.base_damage} + ({main_character.weapon.min_dmg_roll} to {main_character.weapon.max_dmg_roll}) damage!")
    print(f"Your current armor is a {main_character.armor.name}, it is giving you an extra {main_character.armor.value} health points!")
    print(f"Your current health is {main_character.curr_health} out of {main_character.max_health}!")
    separation()

def give_item(item):
    player_inventory.append(item.upper())
    print(f"You have received a {item.upper()}")

#SETS UP PLAYERS INTERACTIVE INVENTORY
player_inventory = []
player_inventory.append("IPHONE")

#DICTIONARY CONTAINING BEGINNING OPTION DESCRIPTIONS
area_descriptions = {
    'closet': 'Nothing but old rags, and dust',
    'door': 'You exit your newfound bedroom and appear to be in a tavern of sorts. It reminds you of Game of Thrones.',
    'window': 'You look outward to see viridian trees, cobblestone paths, and open skies.'}

#BEGIN GAME PROMPT
start_game = input("Do you want to begin your adventure? (yes/no) ").lower().strip()
assert start_game == 'yes' or start_game == 'no', 'Invalid input, please enter "yes" or "no": '
if start_game == 'yes':
    print("Let's begin!")
    separation()
    character_name = input(str("What is your name? "))
    print('Welcome to the world of Creatures & Caverns ' + character_name + ', adventure awaits!')
    separation()
    print('You awake in a strange, though cozy bedroom. You tear off your linen covers and begin to investigate.')
    #WAKE UP IN ROOM LOOK AROUND
    while True:
        begin_answer = input('Where to check? (window/door/closet) ').lower().strip()
        if begin_answer == 'door':
            separation()
            print(area_descriptions['door'])
            break
        elif begin_answer == 'closet':
            separation()
            print(area_descriptions['closet'])
        elif begin_answer == 'window':
            separation()
            print(area_descriptions['window'])
        else: 
            separation()
            invalid_input()
    print('A short and stout man with a very scraggly beard and a heavy accent approaches you with a disagreeable look in his eyes.')
    #DWARF ENCOUNTER
    while True:
        dwarf_answer = input("Who in Kyberia's name are you?! ")
        separation()
        if dwarf_answer == character_name:
            break
        else:
            print("I sniff out lies and treachery a mile away, tell the truth.")
    print("Well " + character_name + ", while you're here you might as well be put to work! Go check the board and make yerself useful!")
    print('You go to the bulletin board you were so kindly directed to and find a job posting to explore the "Doomlit Caverns".')
    print("You tear off the quest posting for 'Doomlit Caverns'! You bring it back to the nameless Dwarf excitedly.")  
    print("Aye so yer ready to take on the caverns huh?")
    #PLAYER GETS WEAPON+ARMOR VIA ANSWER USING IF/ELIF/ELSE, DEPENDING ON ANSWER THEIR CLASSES WEAPON+ARMOR IS UPDATED
    while True:
        print('Anything to say before you go?')
        farewell = input('(Nope/See you in hell/Wish me luck) ').strip().lower()
        if farewell == 'nope':
            separation()
            main_character = Character(character_name, steel_flail, 35, 35, leather_pants, 90, 0, 100)
            print("The silent type? Righty then, you'll be needing this.")
            player_inventory.append(steel_flail.name)
            player_inventory.append(leather_pants.name)
            print(f'You have obtained a {main_character.weapon.name} as your weapon!')
            print(f"You have obtained {main_character.armor.name} as your armor!")
            main_character.curr_health = main_character.max_health
            break
        elif farewell == 'see you in hell':
            separation()
            main_character = Character(character_name, greatsword, 35, 35, leather_pants, 90, 0, 100)
            print("I like yer attitude! Here you are adventurer!")
            player_inventory.append(greatsword.name)
            player_inventory.append(leather_pants.name)
            print(f'You have obtained a {main_character.weapon.name} as your weapon!')
            print(f"You have obtained {main_character.armor.name} as your armor!")
            main_character.curr_health = main_character.max_health
            break
        elif farewell == 'wish me luck':
            separation()
            main_character = Character(character_name, wooden_club, 35, 35, leather_pants, 90, 0, 100)
            print("You'll be needin' a hell of a lot more than luck out there. Here.")
            player_inventory.append(wooden_club.name)
            player_inventory.append(leather_pants.name)
            print(f'You have obtained a {main_character.weapon.name} as your weapon!')
            print(f"You have obtained {main_character.armor.name} as your armor!")
            main_character.curr_health = main_character.max_health
            break
        else:
            separation()
            invalid_input()
    print("Off you go now!")
    separation() 

    #WHERE THE PLAYER HAS THEIR FIRST FIGHT
    print('Confused at how all this happened, you push through the taverns creaky double doors into the warm sunlight.')
    print('As you make your way outside, a small gelatinous figure with an eerily happy grin blocks your path.')
    separation()
    print("Aye laddy! That there's a " + slime1.name + "! He may not look it but he wants trouble! Use your " + main_character.weapon.name + " to teach it a lesson!") 
    print("The slime's overbearing grin turns to a scowl as it lunges at you, get ready to attack!")
    combat(main_character,slime1)

    #PLAYER RECEIVES FIRST ITEM AND LEARNS HOW TO CHECK STATS AND USE INVENTORY
    #STATS TUTORIAL
    print("Not bad for your first fight! Let's see the damage!")
    while True:
        command = input("Type 'STATS' at any time to check your current statistics! Once you've got the hang of it, type 'EXIT' to continue! ").strip().lower()
        if command == 'stats':
            check_stats()
        elif command == 'exit':
            break
        else:
            invalid_input()
            separation()

    #DECIDES WHETHER OR NOT CHARACTER NEEDS HEALTH POTION
    if main_character.curr_health == main_character.max_health:
        print('Not a single scratch! Have this for the road anyway!')
    else:
        print("Nothin' one of these can't fix!")
    give_item('health potion')

    #INVENTORY TUTORIAL
    separation()
    while True:
        command = input("Type 'INVENTORY' any time out of combat to open your inventory! Once you've got the hang of it, type 'EXIT' to continue! ").strip().lower()
        separation()
        if command == 'inventory':
            access_inventory()
        elif command == 'exit':
            break
        else:
            invalid_input()  

    print('Well with that I think yer ready to begin an adventure! Happy trails!')
    separation()

    #DOOMLIT CAVERNS BRANCH
    print(f"Happy with your first encounter, you spot the worn down signs to guide your path. A wooden arrow reading 'DOOMLIT CAVERNS'. Must be the way!")
    print("You walk down a cobblestone path, lined with beautiful vegetation and a cool breeze that brings it to life.")
    print("After nearly a mile of this scenery, it slowly devolves into fog and rocks, and you spot a gaping entrance at the bottom of a valley.")
    #DOUBLE SLIME ENCOUNTER
    print("Out of the woodworks comes a familiar, very joyous face, and it isn't alone. Get ready to strike!")
    separation()
    combat(main_character,normal_slime1)
    print("Nothing you haven't handled before, but here comes another!")
    combat(main_character,normal_slime2)
    print("Whew! You really feel like you're getting the hang of this!")
    print("You catch your breath and head into the assumed 'DOOMLIT CAVERNS', within you spot a chest! ")

    #FIRST CHEST, ROLLS A RANDOM WEAPON/ARMOR/ITEM PULL
    while True:
        chest_input = input("Do you open the chest? (yes/no) ").strip().lower()
        separation()
        if chest_input == 'yes':
            num = roll(0,100)
            if num <= 5:
                print("Nothing? Who leaves an empty chest lying around?!")
                break
            elif num <= 25:
                switch_weapons(twin_daggers)
                break
            elif num <= 65:
                give_item('health potion')
                break
            elif num <= 99:
                switch_armor(vikings_helmet)
                break
            elif num == 100:
                switch_armor(swim_trunks)
                break
            else:
                invalid_input()
        elif chest_input == 'no':
            print("You leave the chest behind.")
            break
        elif chest_input == 'stats':
            check_stats()
        elif chest_input == 'inventory':
            access_inventory()
        else:
            invalid_input()

    separation()
    print("You continue to traverse the cavern, but it's getting darker and quite ominous, good thing you still have your IPHONE on you!")
    #FIRST REAL ATTEMPT TO KILL THE PLAYER, EITHER HAVE TO FIGHT THE BATS OR THEY DIE
    while True:
        bats_encounter = input("Turn on your flashlight? (yes/no) ").strip().lower()
        if bats_encounter == 'stats':
            check_stats()
        elif bats_encounter == 'inventory':
            access_inventory()
        elif bats_encounter == 'yes':
            print("As you scan the room several pairs of small glowing orbs appear, and they're quickly approaching you.")
            print("You then see the small body attached to them...")
            print("You're assaulted by a swarm of BATs!")
            combat(main_character, bat1)
            combat(main_character, bat2)
            combat(main_character, bat3)
            combat(main_character, bat4)
            break
        elif bats_encounter == 'no':
            print("You decide to brave the darkness, only to soon find your feet slipping from the ground beneath you.")
            print("You frantically reach for your IPHONE and turn on the flash light to see you are falling into a pit of some VERY sharp stalagmites.")
            game_over()
        else:
            invalid_input()
    separation()
    print("After you've warded off the miniature army of BATs you look around.")
    print("Good thing you turned on the flashlight, there's a giant pit with stalagmites at the bottom RIGHT next to you, close one!")
    print("You continue onward, soon the granite passage diverges into two, and you're left with a choice!")
    #ANOTHER COMBAT DECISION, EITHER FIND/FIGHT MIMIC CHEST OR FIGHT TROLL (TOUGH)
    while True:
        direction = input("Which way do you go? (left/right) ").strip().lower()
        separation()
        if direction == 'inventory':
            access_inventory()
        elif direction == 'stats':
            check_stats()
        elif direction == 'left':
            print("You continue down the left path, you see another person! Though they're very tall, and ugly, and... GREEN?!")
            combat(main_character, troll)
            print("After defeating the TROLL, you sit down and take a break before continuing your quest.")
            break
        elif direction == 'right':
            print("You continue down the right path and find another chest, it must be your lucky day!")
            while True:
                mimic_encounter = input("Open the chest? (yes/no) ")
                if mimic_encounter == 'inventory':
                    access_inventory()
                elif mimic_encounter == 'stats':
                    check_stats()
                elif mimic_encounter == 'yes':
                    print("As you reach to claim your treasure, the chest is opening all on its own...")
                    print("It's bearing sharp, blood-stained teeth... WATCH OUT!")
                    combat(main_character, mimic)
                    print(f"The MIMIC dropped something!")
                    switch_weapons(iron_hatchet)
                    break
                elif mimic_encounter =='no':
                    print("You examine the chest further and see blood splattered around it's opening, and it has teeth?! You hustle past it...")
                    break
                else:
                    invalid_input()
            break
        else:
            invalid_input()
        separation()

    #SECOND CHEST
    print("You venture deeper into the cavern and find a hollow outing, with no danger in sight you explore it.")
    print("A chest!")
    while True:
        chest_input = input("Do you open the chest? (yes/no) ").strip().lower()
        separation()
        if chest_input == 'yes':
            num = roll(0,100)
            if num <= 5:
                print("Nothing? Who leaves an empty chest lying around?!")
                break
            elif num <= 30:
                give_item('health potion')
                break
            elif num <= 55:
                switch_weapons(brass_knuckles)
                break
            elif num <= 80:
                switch_weapons(warforged_hammer)
                break
            elif num <= 100:
                switch_armor(steel_chestpiece)
                break
            else:
                invalid_input()
        elif chest_input == 'no':
            print("You leave the chest behind.")
            break
        elif chest_input == 'stats':
            check_stats()
        elif chest_input == 'inventory':
            access_inventory()
        else:
            invalid_input()
        separation()

    #SECOND COIN FLIP FOR DEATH
    print("You venture further into the caverns and find a hollow entrance, just barely fitting your body.")
    while True:
        continue_on = input("Enter the opening? (yes/no) ").strip().lower()
        separation()
        if continue_on == 'stats':
            check_stats()
        elif continue_on == 'inventory':
            access_inventory()
        elif continue_on == 'no':
            print("You look to turn back and begin to feel the earth shake beneath you.")
            print("You panic and look to escape into the small entrance, but it's been caved in!")
            print("To the way you entered, but to no avail it's been crumbled as well... and the ceiling is following quickly.")
            game_over()
        elif continue_on == 'yes':
            break
        else:
            invalid_input()
    separation()

    print("You continue forward and feel the ground shake beneath you.")
    print("You turn around to see the entrance is caved in, though a little shaken, you're grateful you made this choice.")
    print("These tremors seem to have shaken the local fauna, as some small critters rush their way past you.")
    separation()
    print("The entrance opens into a larger, damp section of the cave.")

    #TOADS COMBAT
    print("As the critters roll past you, you notice two lumpy beings turn to you, they're some cute toads!")
    print("Their eyelids close sideways and change from the calming yellow they once were to a piercing red, these amphibians mean business.")
    combat(main_character,mud_toad)
    separation()
    print("The other toad lashes out its enormous, and apparently spiked tongue, engulfing the other one's body.")
    print("It doubles in size and is charging at you full speed!!!")
    combat(main_character,large_mud_toad)

    #JUST POSSIBLE LOOT
    print("After you've slain the oversized amphibians, you notice a person's body in the corner, poor guy... but they could have some stuff!")
    while True:
        loot_body = input("Loot the deceased adventurer's corpse? (yes/no) ")
        if loot_body == 'stats':
            check_stats()
        elif loot_body == 'inventory':
            access_inventory()
        elif loot_body == 'no':
            print("You decide grave robbing isn't your thing and continue onward.")
            break
        elif loot_body == 'yes':
            switch_armor(obsidian_gauntlets)
            switch_weapons(steamtech_gloves)
            give_item('health potion')
            break
        else:
            invalid_input()
        
    #BEGIN TRAVELING TO THE FINAL BOSS
    #CHANCE TO HEAL        
    while True:
        menu_chance = input("What do you do now? (look around/sit down) ")
        if menu_chance == 'stats':
            check_stats()
        elif menu_chance == 'inventory':
            access_inventory()
        elif menu_chance == 'look around' or 'sit down':
            break
        else:
            invalid_input()


    print("Moving away from the corpse, you notice the tremors begin again, but much more faint.")
    print("As you look around you notice there appears to be no exit... not even the way you entered.")
    print("You search and search, but to no avail... That's when you watch the corpse get swallowed by the ground beneath you.")
    print("From beneath the vortex of sand emerges a monstrous bipedal insect, and it doesn't look friendly, prepare for battle!")
    combat(main_character, hulkering_umbra)
    
    print("Congratulations, you've defeated the final boss! Thank you for playing Creatures and Caverns!")

else:
    print("That's too bad! See you next time!")