from sys import exit

def quest_start(quest,role,lvl,trophy):
    if quest == "Dragon":
        Dragon(role, lvl, trophy)
    elif quest == "Emperor":
        Emperor(role, lvl, trophy)
    elif quest == "Ghost":
        Ghost(role, lvl, trophy)

def Dragon(role , lvl, trophy):
    """Dragon story, which role wins? """
    print "You find the dragon in its hovel, do you attack or run?"
    if role == "mage" and lvl == 1:
        lvl += 1
        print "You begin to cast but then the dragon takes your arm. You flee, corterize your wound and begin a new quest"
        choice == raw_input("> Do you choose the Emperor or the Ghost next?")
        if choice == "Emperor" or "Ghost":
            if choice == "Emperor":
                Emperor()
            else:
                Ghost()
        else:
            "Error"
            exit(0)
    elif role == "warrior" and lvl == 1:
        print "You charge in, parry the dragon's fire with your shield. Then manage to slay him at the last moment, Good job"
        lvl += 2
        choice == raw_input("> Do you choose the Emperor or the Ghost next?")
        if choice == "Emperor" or "Ghost":
            if choice == "Emperor":
                Emperor()
            else:
                Ghost()
        else:
            "Error"
            exit(0)
    elif role == "archer" and lvl == 1:
        lvl += 1
        print "You shoot an arrow and it bounces off his scales. The Dragon stares curiously, and goes back to sleeping. You return home in shame"
        choice == raw_input("> Do you choose the Emperor or the Ghost next?")
        if choice == "Emperor" or "Ghost":
            if choice == "Emperor":
                Emperor()
            else:
                Ghost()
        else:
            "Error"
            exit(0)
    else:
        print "Error"
        exit(0)

def Ghost(role, lvl, trophy):
    """Ghost funciton, takes arguments of role and lvl"""
    if role == "warrior" or "mage" or "archer":
        if role == "warrior":
            print "You are level %s and your inventory has %s" %(lvl,trophy)
            if lvl < 2:
                lvl += 1
                print "You swing into the ghost and it glides through your sword"
                print "You become cursed, but survive"

            elif lvl > 2 and lvl < 4:
                if "dragon's head" in trophy:
                    lvl += 2
                    print " Armed with the Dragon enhancement, your sword glows with the dragon's power and you slay it "
                    trophy.append("spirit of the ghost")
                    print "Now onto the final boss!"
                    Emperor(role,lvl,trophy)
                else:
                    print "eror"
                    exit(0)

        if role == "mage":
            if lvl > 2:
                print "You cast an ancient spell known only to your master! It's highly effective and the Ghost dissappears"
                lvl += 2
                trophy.append('Ghost Essence')
            elif lvl < 2:
                if "Emperor's treasure" and "Dragon Spirit" in trophy:
                    print "Using Emperor's treasure, you cast a special spell that exorcises the ghost. Finally you transform into a dragon using the spirit to cleasne the ashes"
                    lvl += 2
                    trophy.append('Ghost Essence')
                    winner()
                elif "Dragon Spirit" in trophy:
                    print "You cast a spell that transforms you into a dragon"
                    print """You burn fight the Ghost using your ult flam ability. It is not known if the Ghost is actually gone"""
                    print "As you are about to leave you notice you have acquired 'Ghost Essence'. Now off to the Emperor ! "
                    lvl += 1
                    trophy.append('Ghost Essence')
                elif "Emperor's treasure" in trophy:
                    print "Using Emperor's treasure, you cast a special spell that exorcises the ghost. An unholy aura envelops you"
                    lvl += 1
                    trophy.append('Ghost Essence')
                    print "Now to defeat the Dragon in it's lair"
                    Dragon(role,lvl,trophy)

def role_check(role, check):
    """Checks the role by assigning value to each class"""
    if role == "mage":
        check = 1
    elif role == "warrior":
        check = 1
    elif role == "archer":
        check = 1
    else:
        while check!= 1:
            if role == "mage":
                check = 1
            elif role == "warrior":
                check = 1
            elif role == "archer":
                check = 1

def quest_check(quest, check):
    """Checks the quest by assigning value to each class"""
    if quest == "Dragon":
        check = 1
    elif quest == "Ghost":
        check = 1
    elif quest == "Emperor":
        check = 1
    else:
        while check != 1:
            if quest == "Dragon":
                check = 1
            elif quest == "Ghost":
                check = 1
            elif quest == "Emperor":
                check = 1


print "Welcome, you will now bring begin your journey"
print "What is your name?"
name = raw_input("> ")

print "Welcome then, %s. May you prevail. Are you a mage, archer, or warrior?" % name
role = raw_input("> ")
check = 0


role_check(role,check)

lvl = 1
trophy = []

print "Would you like to attack the Dragon, Emperor, or Ghost"
quest = raw_input = ("> ")
check = 0

quest_check(quest,check)

quest_start(quest,role,lvl,trophy)

print "right, lets move forward with %s" % quest
