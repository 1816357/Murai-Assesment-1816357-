# GAME

# Game State
gameState = 1

# PLAYER INFO

# Player Stats
player1 = {'Name': 'Murai', 'Health': 100, 'Level': 0, 'Exp': 0}

# Inventory

# Weapons
playerWeapon1 = {'Weapon1': 'W1', 'AttackPower': '0'}

playerWeapon2 = {'Weapon2': 'W2', 'AttackPower': '0'}

playerWeapon3 = {'Weapon2': 'W3', 'AttackPower': '0'}

# Health
playerHealthItemSmall = {'Med-kit': 'Small Med-kit', 'Plus Health': 30}
maxSmallmed = 5

playerHealthItemBig = {'Med-kit': 'Big Med-kit', 'Plus Health': 100}
maxBigmed = 3
# ENEMIES

# Enemy Stats
enemy1 = {'Name': 'enemyOne', 'Health': 100, 'Exp': 10}

enemy2 = {'Name': 'enemyTwo', 'Health': 100, 'Exp': 50}

enemy3 = {'Name': 'enemyThree', 'Health': 100, 'Exp': 100}

enemy4 = {'Name': 'enemyFour', 'Health': 100, 'Exp': 500}

enemy5 = {'Name': 'enemyFive', 'Health': 100, 'Exp': 1000}

# civilians

civilian1 = {'Name': 'civOne', 'Exp': 30}

civilian2 = {'Name': 'civTwo', 'Exp': 30}

civilian3 = {'Name': 'civTwo', 'Exp': 30}

civilian4 = {'Name': 'civThree', 'Exp': 30}

civilian5 = {'Name': 'civFour', 'Exp': 30}

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
    of smoke is gradually getting stronger and the sense that something is wrong gets
    overwhelms you.
    \nPlayer Options: \n1) Run to the village\n:""")
    if user_input.lower() == "run back to the village":
        gameState = 2.1

while gameState == 2.1:
    user_input = input("""
    You've finally arrived at Ringo to see your village Up in smoke, fire going as far 
    as the eye can see. The village guardians on the ground dead along with the villagers 
    either dead or seriously injured. You hear screams
    
    \nPlayer Options: \n1) Run\n:""")
    if user_input.lower() == "run":
        gameState = 2.2