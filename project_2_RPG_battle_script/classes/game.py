import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        '''
        initial
        :param hp: hp
        :param mp: mana
        :param atk: attack
        :param df: defence
        :param magic: magic
        '''
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.magic = magic
        self.df = df
        self.action = ["Attack", "Magic", "Items"]
        self.items = items

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def heal(self, dmg):
        self.hp += dmg
        if self.hp >= self.get_max_hp():
            self.hp = self.get_max_hp()

    def choose_action(self):
        i = 1
        print("\n" + self.name)
        print(bcolors.BOLD + bcolors.OKBLUE + "ACTION:" + bcolors.ENDC)
        for item in self.action:
            print("    " + str(i) + "." + item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.BOLD + bcolors.OKBLUE + "MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + "." + spell.name, "cost: " + str(spell.cost))
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.BOLD + bcolors.OKGREEN + "ITEM:" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ":" + item["item"].name, item["item"].description, "(x" + str(item["quantity"]) + ")")
            i += 1

    def get_stats(self):
        hp_bar = ""
        mp_bar = ""
        hp_bar_sticks = self.hp / self.maxhp * 100 / 4
        mp_bar_sticks = self.mp / self.maxmp * 100 / 10

        while hp_bar_sticks > 0:
            hp_bar += "█"
            hp_bar_sticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_sticks > 0:
            mp_bar += "█"
            mp_bar_sticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        print(bcolors.BOLD + self.name + ":\t\t\t" + str(self.hp) +"/" + str(self.maxhp) + "\t|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|\t\t" + str(self.mp) + "/" + str(self.maxmp) + "\t|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
