# GAME

# Game State
# import random

gameState = 1

# PLAYER INFO

# Player Stats
player1 = {'Player': 'Murai', 'Health': 100, 'Level': 0, 'Exp': 0}

# Inventory

# Weapons
primaryWeapon1 = {'Primary Weapon': 'W1', 'Attack One': 1, 'Attack Two': 0, 'Attack Three': 0}

secondaryWeapon1 = {'Secondary Weapon': 'S2', 'AttackOne': 0, 'AttackTwo': 0, 'AttackThree': 0}

playerWeapon3 = {'Weapon3': 'W3', 'AttackOne': 0, 'AttackTwo': 0, 'AttackThree': 0}

# Health
playerHealthItemSmall = {'Med-kit': 'Small Med-kit', 'How Many': 0, 'Plus Health': 30}
maxSmallmed = 5

playerHealthItemBig = {'Med-kit': 'Big Med-kit', 'Plus Health': 100}
maxBigmed = 3
# ENEMIES

# Enemy Stats
enemy1 = {'enemy1': 'enemyOne', 'Health': 100, 'Exp': 10}

enemy2 = {'enemy2': 'enemyTwo', 'Health': 100, 'Exp': 50}

enemy3 = {'enemy3': 'enemyThree', 'Health': 100, 'Exp': 100}

enemy4 = {'enemy4': 'enemyFour', 'Health': 100, 'Exp': 500}

enemy5 = {'enemy5': 'enemyFive', 'Health': 100, 'Exp': 1000}

# civilians

civilian1 = {'Name': 'civOne', 'Exp': 30}

civilian2 = {'Name': 'civTwo', 'Exp': 30}

civilian3 = {'Name': 'civTwo', 'Exp': 30}

civilian4 = {'Name': 'civThree', 'Exp': 30}

civilian5 = {'Name': 'civFour', 'Exp': 30}

hasKilled = 1
# Random

# One
# import random

# enemyOneAnswers = ["Answer One\n", "Answer Two\n", "Answer Three\n"]
#
# playerOneQuestions = ["Who are you?", "Question Two", "Question Three"]
#
# # Two
# enemyTwoAnswers = ["Answer One\n", "Answer Two\n", "Answer Three\n"]
# playerTwoQuestions = ["Question One", "Question Two", "Question Three"]
#
# # Three
# enemyThreeAnswers = ["Answer One\n", "Answer Two\n", "Answer Three\n"]
# playerThreeQuestions = ["Question One", "Question Two", "Question Three"]


# After You and a few other villagers
#     dealt with the fire, the rebuilding of the village barrier, gathering the dead bodies
#     and tending to the those who are injured you begin to feel exhausted.

# Story

while gameState == 1:
    user_input = input("Type Play To Begin\n:")
    if user_input.lower() == "play":
        print("intro")
        gameState = 2

while gameState == 2:
    user_input = input("""
    Your on your way back to Ringo from a hunting job. Nothing seems out of the ordinary. 
    As you get closer you begin to notice that the sky is getting darker and the smell 
    of smoke is gradually getting stronger. The sense that something is wrong begins
    overwhelm you.
    
    What do you do?
    
    \nPlayer Options: \n1) Run back to the village\n:""")
    if user_input.lower() == "run back to the village":
        gameState = 2.1
    else:
        print("Enter a viable option")

while gameState == 2.1:
    user_input = input("""
    You've finally arrived at Ringo to see your village Up in smoke, fire going as far 
    as the eye can see. The village guardians on the ground dead along with villagers 
    either dead or seriously injured. You hear a desperate scream for help East off of 
    the Village Gate. 
    
    What do you do?
    
    \nPlayer Options: \n1) North\n2) East\n3) South\n4) West\n:""")

    # if user_input.lower() == "north":
    #     gameState = 2.3

    if user_input.lower() == "east":
        gameState = 2.4
    #
    # if user_input.lower() == "South":
    #     gameState = 2.3
    # else:
    #     print("Enter a viable option")
    #
    # if user_input.lower() == "West":
    #     gameState = 2.3
    # else:
    #     print("Enter a viable option")

while gameState == 2.4:
    user_input = input("""
    You've run towards the screams to find a group of three masked assailants covered in
    blood wielding swords on the verge of attacking a mother and her child.
    
    There are three weapons in close proximity to you. A Sword, Spear, and Dagger.

    Which weapon do you pick up?
    
    \nPlayer Options: \n1) Sword\n2) Spear\n3) Dagger\n:""")

# Sword
    if user_input.lower() == "sword":
        primaryWeapon1['Primary Weapon'] = 'Sword'
        primaryWeapon1['Attack One'] = 27
        primaryWeapon1['Attack Two'] = 18
        primaryWeapon1['Attack Three'] = 33
        print("""

        You have chosen the Sword as your primary weapon

        """)
        gameState = 2.5
# Spear
    if user_input.lower() == "spear":
        primaryWeapon1['Primary Weapon'] = 'Spear'
        primaryWeapon1['Attack One'] = 30
        primaryWeapon1['Attack Two'] = 22
        primaryWeapon1['Attack Three'] = 36
        print("""

        You have chosen the Spear as your primary weapon

        """)
        gameState = 2.5
# Dagger
    if user_input.lower() == "dagger":
        primaryWeapon1['Primary Weapon'] = 'dagger'
        primaryWeapon1['Attack One'] = 15
        primaryWeapon1['Attack Two'] = 11
        primaryWeapon1['Attack Three'] = 20
        print("""

        You have chosen the Dagger as your primary weapon

        """)
        gameState = 2.5

while gameState == 2.5:

    user_input = input("""
    After seeing all the destruction that has been done to the village, rage just fills 
    your whole body. 
    
    You leap at one of them taking one of them out with ease and watch his lifeless
    body hit the ground. 
    
    The other two turn towards you realising one of them have been killed.
    
    One of the masked assailants jumps at you and the fight begins.

    \nPlayer Options: \n1) Start Fight\n:""")

    if user_input.lower() == "start fight":
        print("\n")
        gameState = 2.6

while gameState == 2.6:
    print("Fight One\n")
    print(player1)
    print("\n")

    for key, value in primaryWeapon1.items():
        print(key, ':', value)
    gameState = 2.7
    break

while gameState == 2.7:

    user_input = input("""Enter Attack:""")

    for key in primaryWeapon1.items():
        if user_input.lower() == 'attack one':
            enemy1['Health'] = (enemy1.get('Health') - primaryWeapon1.get('Attack One'))
            player1['Health'] = (player1.get('Health') - 10)
            print("\n")
            print(player1)
            print("\n")
            print(enemy1)

        if user_input.lower() == 'attack two':
            enemy1['Health'] = (enemy1.get('Health') - primaryWeapon1.get('Attack Two'))
            player1['Health'] = (player1.get('Health') - 12)
            print("\n")
            print(player1)
            print("\n")
            print(enemy1)

        if user_input.lower() == 'attack three':
            enemy1['Health'] = (enemy1.get('Health') - primaryWeapon1.get('Attack Three'))
            player1['Health'] = (player1.get('Health') - 14)
            print("\n")
            print(player1)
            print("\n")
            print(enemy1)

        if enemy1['Health'] <= 0:
            player1['Exp'] = (player1.get('Exp') + enemy1.get('Exp'))
            print("\n")
            print("+10Exp\n")
            gameState = 3
        break
#
while gameState == 3:
    # mention something about same the family here
    user_input = input("""
    With another one down the last assailant is frozen in place realising it might be the
    end for him. 
    
    Your left with the choice to either Kill or Capture him for questioning.

    What do you do?
    
    \nPlayer Options: \n1) Capture\n2) Kill\n:""")

    if user_input.lower() == 'capture':
        gameState = 3.1

    if user_input.lower() == 'kill':
        hasKilled = 2
        gameState = 3.2

while gameState == 3.1:
    print("""
    You've chosen to keep the man alive for the moment.\n""")
    gameState = 3.3
    break

while gameState == 3.2:
    print("""
    You've chosen to Kill the man.\n""")
    gameState = 3.3
    break

while gameState == 3.3:
    user_input = input("""
    After You and a few other villagers dealt with the fire, the rebuilding of the village 
    barrier, gathering the dead bodies and tending to the those who are injured you begin 
    to feel exhausted.

    \nPlayer Options: \n1) Next\n:""")

    if user_input.lower() == 'next':
        gameState = 3.4

while gameState == 3.4:
    user_input = input("""
    It's beginning to get dark, You and the few other member of the village call it for the
    day and head to the village centre for food and warmth.

    As you get closer you begin to notice the how much the number of villagers shrunk.
    
    The state of them and the look of their faces pains you.
    
    You debate on whether you should head to the village camp fire or head straight to 
    bed after everything that's happened today.

    What do you do?
    
    \nPlayer Options: \n1) Take a seat around the village camp fire\n2) Head back to bed\n:""")

    if user_input.lower() == 'take a seat around the village camp fire':
        player1['Exp'] = (player1.get('Exp') + 20)
        print("+20Exp")
        print(player1)
        gameState = 3.5

    if user_input.lower() == 'head back to bed':
        if hasKilled == 1:
            gameState = 5

        if hasKilled == 2:
            gameState = 6

while gameState == 3.5:
    user_input = input("""
    You walk over to take a seat around the camp fire. As you sit down you feel the heat
    resonate throughout you entire body, you can sense that the moral is low.

    While you eating dinner Your approached by two people. As they get closer to you you
    realise that it's the mother and the child you just saved.

    They thank you for saving them by they offer you a gift.

    What do you do?
    
    \nPlayer Options: \n1) Accept\n2) Decline\n:""")

    if user_input.lower() == 'accept':
        if hasKilled == 1:
            print("You've received a Healing Item\n")
            playerHealthItemSmall['How Many'] = (playerHealthItemSmall.get('How Many') + 1)
            print(playerHealthItemSmall)
            gameState = 3.6

        if hasKilled == 2:
            print("You've received a Healing Item\n")
            playerHealthItemSmall['How Many'] = (playerHealthItemSmall.get('How Many') + 1)
            print(playerHealthItemSmall)
            gameState = 6

    if user_input.lower() == 'decline':
        if hasKilled == 1:
            gameState = 3.6

        if hasKilled == 2:
            gameState = 6

while gameState == 3.6:
    user_input = input("""
    There is some chatter around the camp fire but it's not enough to fill the silence.
    
    You've just finished eating and you get up.

    What do you do?
    \nPlayer Options: \n1) Question the Masked Assailant\n2) Leave it for tomorrow\n:""")

    if user_input.lower() == 'question the masked assailant':
        gameState = 4

    if user_input.lower() == 'leave it for tomorrow':
        gameState = 5

while gameState == 4:
    user_input = input("""
    Your about to question the masked assailant but before you get there village warning
    bells go off. 
    
    You think it's another attack...that the hut where the masked assailant is in has been set
    on fire.

    \nPlayer Options: \n1) Help put the fire out\n:""")

    if user_input.lower() == "help put the fire out":
        gameState = 4.1

while gameState == 4.1:
    user_input = input("""
    You and few other villagers have put out the fire before it could spread even more.
    

    \nPlayer Options: \n1) Next\n:""")
    if user_input.lower() == "next":
        if hasKilled == 1:
            gameState = 7

        # if hasKilled == 2:
        #     gameState = 7

while gameState == 5:
    user_input = input("""
                                        Day Two: I you captured the guy

    A ray of light hits your face waking you up... and you realise the smell of smoke
    is still in the air and... is silent, the sounds of children playing outside isn't
    there anymore instead you can hear the wind brush the ground...

    What do you do?

    \nPlayer Options: \n1) Get Up\n2) Lay in\n:""")

    if user_input.lower() == 'get up':
        gameState = 5.1

    if user_input.lower() == 'lay in':
        gameState = 5.2


while gameState == 5.1:
    user_input = input("""
    You get up and go outside to find ...the news that the masked assailant was murdered
    during the night.

    \nPlayer Options: \n1) Go check on the Masked Assailant\n:""")

    if user_input.lower() == 'go check on the masked assailant':
        gameState = 7

while gameState == 5.2:
    user_input = input("""
    A Couple hours Later a village elder knocks on your door waking you up. She tells
    you that the masked assailant was murdered during the night.

    \nPlayer Options: \n1) Go check on the Masked Assailant\n:""")

    if user_input.lower() == 'go check on the masked assailant':
        gameState = 7

# I you killed the guy
while gameState == 6:
    user_input = input("""
                                        Day Two: I you killed the guy

    A ray of light hits your face waking you up...and you realise the smell of smoke
    is still in the air and... is silent, the sounds of children playing outside isn't
    there anymore instead you can hear the wind brush the ground...

    You begin to get curious... about the men... get up and investigate

    What do you do?

    \nPlayer Options: \n1) Get up\n:""")

    if user_input.lower() == 'get up':
        gameState = 7

while gameState == 7:
    user_input = input("""
    You decide to check on the body to see what remains and something silver catches your eye.
    

    \nPlayer Options: \n1) Pick up and Inspect\n:""")

    if user_input.lower() == 'pick up and inspect':
        gameState = 7.1

while gameState == 7.1:
    user_input = input("""
    It's a silver medallion with an insignia printed on it.
    
    The insignia belongs to a raider Clan...

    \nPlayer Options: \n1) Next\n:""")

    if user_input.lower() == 'next':
        gameState = 7.2

while gameState == 7.2:
    user_input = input("""
    You leave the village in pursuit of these
    \nPlayer Options: \n1) Next\n:""")

    if user_input.lower() == 'next':
        gameState = 7.3

while gameState == 7.3:
    user_input = input("""
    You've been walking for a while now there and now reached a cross-road.
    there are three paths you can take.
    
    Which path do you take?
    \nPlayer Options: \n1) Left\n2) Middle\n3) Right\n:""")

    if user_input.lower() == 'left':
        print("""
        \nYou have chosen the path on the left""")
        gameState = 8

    if user_input.lower() == 'middle':
        gameState = 8.4

    # if user_input.lower() == 'right':
    #     gameState =

while gameState == 8:
    user_input = input("""
    On Your journey to hunt those individuals down you've you hear someone screaming for help
    
    \nPlayer Options: \n1) Run towards the screams\n:""")

    if user_input.lower() == 'run towards the screams':
        gameState = 8.1

while gameState == 8.1:
    user_input = input("""
    You find out that it's a skinny man trying to fend of a bear the size of a grown adult 
    with a guitar.
    
    What do you do?
    \nPlayer Options: \n1) Watch and laugh\n2) Fight the bear\n3) Make a Loud noise\n:""")

    if user_input.lower() == 'watch and laugh':
        gameState = 8.2

    if user_input.lower() == 'fight the bear':
        gameState = 8.3

    # if user_input.lower() == 'Make a Loud noise':
    #     gameState = 8.4

while gameState == 8.2:
    user_input = input("""
    While your laughing at him you hear some rustling bushes to your left.
    
    it's the bears mother and it's the size of...
    
    She Claws at him, but  you... to push him out of the way.
    
    \nPlayer Options: \n1) Start Fight\n:""")
    if user_input.lower() == 'start fight':
        if playerHealthItemSmall['How Many'] > 0:
            gameState = 8.3

    if user_input.lower() == 'start fight':
        if playerHealthItemSmall['How Many'] == 0:
            gameState = 9

while gameState == 8.3:
    user_input = input("""
    Use Health Your Health Item before you get into a fight
    
    \nPlayer Options: \n1) Apply Healing Item\n:""")
    if user_input.lower() == 'apply healing item':
        player1['Health'] = (player1.get('Health') + playerHealthItemSmall['Plus Health'])

        gameState = 9

while gameState == 9:
    print("\nFight One\n")
    print(player1)
    print("\n")

    for key, value in primaryWeapon1.items():
        print(key, ':', value)
    gameState = 9.1
    break

while gameState == 9.1:

    user_input = input("""\nEnter Attack:""")

    for key in primaryWeapon1.items():
        if user_input.lower() == 'attack one':
            enemy2['Health'] = (enemy2.get('Health') - primaryWeapon1.get('Attack One'))
            player1['Health'] = (player1.get('Health') - 10)
            print("\n")
            print(player1)
            print("\n")
            print(enemy2)

        if user_input.lower() == 'attack two':
            enemy2['Health'] = (enemy2.get('Health') - primaryWeapon1.get('Attack Two'))
            player1['Health'] = (player1.get('Health') - 12)
            print("\n")
            print(player1)
            print("\n")
            print(enemy2)

        if user_input.lower() == 'attack three':
            enemy2['Health'] = (enemy2.get('Health') - primaryWeapon1.get('Attack Three'))
            player1['Health'] = (player1.get('Health') - 14)
            print("\n")
            print(player1)
            print("\n")
            print(enemy2)

        if enemy2['Health'] <= 0:
            player1['Exp'] = (player1.get('Exp') + enemy2.get('Exp'))
            print("\n")
            print("+10Exp\n")
            gameState = 9.1
        break

while gameState == 9.1:
    user_input = input("""
    The man thanks you for saving him...
    complete""")

while gameState == 8.4:
    user_input = input("""
    You've been walking for a while... and you noticed that it's beging to get dark... faint light
    complete
    \nPlayer Options: \n1) Approach the light\n:""")

while gameState == 8.5:
    user_input = input("""
    Speaking Tree
    \nPlayer Options: \n1) Grass Blade\n2) Wooden Mace\n3) Earth Gauntlets\n:""")

# Grass Blade
    if user_input.lower() == "grass blade":
        primaryWeapon1['Primary Weapon'] = 'Grass Blade'
        primaryWeapon1['Attack One'] = 27
        primaryWeapon1['Attack Two'] = 18
        primaryWeapon1['Attack Three'] = 33
        print("""

        You have chosen the Grass Blade as your primary weapon

        """)
        gameState = 2.5

# Wooden Mace
    if user_input.lower() == "wooden mace":
        primaryWeapon1['Primary Weapon'] = 'Wooden Mace'
        primaryWeapon1['Attack One'] = 30
        primaryWeapon1['Attack Two'] = 22
        primaryWeapon1['Attack Three'] = 36
        print("""

        You have chosen the Wooden Mace as your primary weapon

        """)
        gameState = 2.5

# Earth Gauntlets
    if user_input.lower() == "earth gauntlets":
        primaryWeapon1['Primary Weapon'] = 'earth gauntlets'
        primaryWeapon1['Attack One'] = 15
        primaryWeapon1['Attack Two'] = 11
        primaryWeapon1['Attack Three'] = 20
        print("""

        You have chosen the Earth Gauntlets as your primary weapon

        """)
        gameState = 2.5
#         
# while gameState == 5.1:
#     user_input = input("""
#     You get up and go outside to find ... the news that the masked assailant was murdered
#     during the night.
#
#     Where do you do?
#     \nPlayer Options: \n1)Next\n:""")
#
#     if user_input.lower() == 'next':
#         gameState = 5.3
#
# while gameState == 5.2:
#     user_input = input("""
#     A Couple hours Later a  village elder knocks on your door waking you up... she tells
#     you that the masked assailant was murdered...
#
#     Where do you do?
#     \nPlayer Options: \n1)Next\n:""")
#
#     if user_input.lower() == 'next':
#         gameState = 5.3

#  If you've chosen to kill the masked man.
#     print(random.choice(enemyOneAnswers))
#     user_input = input("""
#     You've captured
#
#     What do you do?
#     \nPlayer Options: \n1) Who are you?\n2) What are you doing here?\n3) Hit him across the face a couple times\n: """)
#
#     if user_input == "Who are you?":
#         pass
#
#     if user_input == "What are you doing here?":
#         pass
#
#     if user_input == "Hit him across the face":
#         print("the captured assailant ")
#         gameState = 3.2
#
# while gameState == 3.2:
#
#     print(random.choice(enemyTwoAnswers))
#     user_input = input("""
#     Story Line
#
#     What do you do?
#     \nPlayer Options: \n1) Question One \n2) Question Two \n3) Question Three\n: """)
#
#     if user_input == "Question One":
#         pass
#
#     if user_input == "Question Two":
#         pass
#
#     if user_input == "Question Three":
#         print("")
#         gameState = 3.3
#
# while gameState == 3.3:
#
#     print(random.choice(enemyThreeAnswers))
#     user_input = input("""
#     Story Line
#
#     What do you do?
#     \nPlayer Options: \n1) Question One \n2) Question Two \n3) Question Three\n: """)
#
#     if user_input == "Question One":
#         pass
#
#     if user_input == "Question Two":
#         pass
#
#     if user_input == "Question Three":
#         print("")
#         gameState = 3.4
