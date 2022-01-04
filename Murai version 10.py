# GAME

# Game State
import random

gameState = 1

# PLAYER INFO

# Player Stats
player1 = {'Player': 'Murai', 'Health': 100, 'Level': 0, 'Exp': 0}

# Inventory

# Weapons
primaryWeapon1 = {'Primary Weapon': 'W1', 'AttackOne': 1, 'AttackTwo': 0, 'AttackThree': 0}

playerWeapon2 = {'Weapon2': 'W2', 'AttackOne': 0, 'AttackTwo': 0, 'AttackThree': 0}

playerWeapon3 = {'Weapon3': 'W3', 'AttackOne': 0, 'AttackTwo': 0, 'AttackThree': 0}

# Health
playerHealthItemSmall = {'Med-kit': 'Small Med-kit', 'Plus Health': 30}
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

# Random

# One
import random
enemyOneAnswers = ["Answer One\n", "Answer Two\n", "Answer Three\n"]

playerOneQuestions = ["Who are you?", "Question Two", "Question Three"]

# Two
enemyTwoAnswers = ["Answer One\n", "Answer Two\n", "Answer Three\n"]
playerTwoQuestions = ["Question One", "Question Two", "Question Three"]

# Three
enemyThreeAnswers = ["Answer One\n", "Answer Two\n", "Answer Three\n"]
playerThreeQuestions = ["Question One", "Question Two", "Question Three"]

# Story

while gameState == 1:
    user_input = input("Type Play To Begin\n:")
    if user_input.lower() == "play":
        print("intro")
        gameState = 2

while gameState == 2:
    user_input = input("""
    Your on your way back to Ringo from a hunting job. Nothing seem out of the ordinary. 
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
    \nPlayer Options: \n1) Run towards the screams\n:""")

    if user_input.lower() == "run towards the screams":
        gameState = 2.2
    else:
        print("Enter a viable option")

while gameState == 2.2:
    user_input = input("""
    You've run towards the screams to find a group of three masked assailants covered in
    blood wielding swords about to attack a mother and her child. There are three weapons
    in close proximity to you. A Sword, Spear, and Twin Daggers.
    
    Which weapon do you pick up?
    \nPlayer Options: \n1) Sword\n2) Spear\n3) Twin Daggers\n:""")

# Sword
    if user_input.lower() == "sword":
        primaryWeapon1['Primary Weapon'] = 'Sword'
        primaryWeapon1['AttackOne'] = 30
        primaryWeapon1['AttackTwo'] = 25
        primaryWeapon1['AttackThree'] = 35
        print("""

        You have chosen the Sword as your primary weapon

        """)
        gameState = 2.3
# Spear
    if user_input.lower() == "spear":
        primaryWeapon1['Primary Weapon'] = 'Spear'
        primaryWeapon1['AttackOne'] = 30
        primaryWeapon1['AttackTwo'] = 25
        primaryWeapon1['AttackThree'] = 35
        print("""

        You have chosen the Spear as your primary weapon

        """)
        gameState = 2.3
# Dagger
    if user_input.lower() == "twin daggers":
        primaryWeapon1['Primary Weapon'] = 'Twin Dagger'
        primaryWeapon1['AttackOne'] = 30
        primaryWeapon1['AttackTwo'] = 25
        primaryWeapon1['AttackThree'] = 35
        print("""
        
        You have chosen the Twin Daggers as your primary weapon
        
        """)
        gameState = 2.3

while gameState == 2.3:

    user_input = input("""
    ... filled with rage you leap at one of them taking on of them out with ease, watching his 
    lifeless body hit the ground. The other two turn towards you realising one of them have been 
    killed. One of the masked assailants jumps at you... and the fight begins.  
    
    \nPlayer Options: \n1) Fight\n:""")

    if user_input.lower() == "fight":
        print("\n")
        gameState = 2.4

while gameState == 2.4:
    print("Fight One\n")
    print(player1)
    print("\n")

    for key, value in primaryWeapon1.items():
        print(key, ':', value)
    gameState = 2.5
    break

while gameState == 2.5:

    user_input = input("""Enter Attack:""")

    for key in primaryWeapon1.items():
        if user_input.lower() == 'attackone':
            enemy1['Health'] = (enemy1.get('Health') - primaryWeapon1.get('AttackOne'))
            print("\n")
            print(enemy1)

        if user_input.lower() == 'attacktwo':
            enemy1['Health'] = (enemy1.get('Health') - primaryWeapon1.get('AttackTwo'))
            print("\n")
            print(enemy1)

        if user_input.lower() == 'attackthree':
            enemy1['Health'] = (enemy1.get('Health') - primaryWeapon1.get('AttackThree'))
            print("\n")
            print(enemy1)

        if enemy1['Health'] <= 0:
            player1['Exp'] = (player1.get('Exp') + enemy1.get('Exp'))
            print("\n")
            print(player1)
            gameState = 3
        break

while gameState == 3:
    # mention something about same the family here
    user_input = input("""
    With another one down the last assailant is frozen in place realising it might be the end 
    for him. Your left with the choice to either KILL or CAPTURE him for questioning.
    
    What do you do?
    \nPlayer Options: \n1) KILL\n2) CAPTURE\n:""")

    if user_input.lower() == 'kill':
        gameState = 6

    if user_input.lower() == 'capture':
        gameState = 3.1

while gameState == 3.1:
    user_input = input("""
    You've chosen to keep him alive for the moment. After You and a few other villagers... 
    dealt with the fire, the rebuilding the village barrier, gathering the dead bodies and tending to 
    the those who are injured... you feel exhausted, ... and tired.

    \nPlayer Options: \n1) Next\n:""")

    if user_input.lower() == 'next':
        gameState = 3.2

while gameState == 3.2:
    user_input = input("""
    You and... call it for the day and head to the village centre for food and warmth.
    
    You see the... has shrunk the... the state of them, the look on their faces... you can't face them...
    after everything that's happened today.
    
    What do you do?
    \nPlayer Options: \n1) Take a seat around the village camp fire \n2) Head back to the Chiefs Quaters\n:""")

    if user_input.lower() == 'take a seat around the village camp fire':
        gameState = 3.3

    if user_input.lower() == 'head back to the Chiefs quarters':
        gameState = 4


#
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
