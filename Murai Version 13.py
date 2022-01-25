# GAME 1

# Game State
# import random

gameState = 0

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

playerHealthItemBig = {'Med-kit': 'Big Med-kit', 'How Many': 0, 'Plus Health': 100}

# ENEMIES

# Enemy Stats
enemy1 = {'enemy1': 'enemyOne', 'Health': 100, 'Exp': 10}

enemy2 = {'enemy2': 'enemyTwo', 'Health': 150, 'Exp': 50}

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
scouted = 1
weaponCounter = 0

# Random

import random
enemyOneAnswers = ["what's going on?", "Were am I?", "Who are you?"]

enemyTwoAnswers = ["WHO ARE YOU?", "WHAT!??", "I don't know what's going on but UNTIE ME NOW!!!!"]

enemyThreeAnswers = ["I Did not expect this", "...", "Just do it already"]

enemyFourAnswers = ["Not my eye!!!", "add string", "add string"]

enemyFiveAnswers = ["add string", "add string", "add string"]

enemySixAnswers = ["add string", "add string", "add string"]

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


# This is the Start of the game. You have to type play to begin.
# Your given a introduction to story and the character.
while gameState == 1:
    user_input = input("Type Play To Begin\n:")
    if user_input.lower() == "play":
        print("intro")
        gameState = 2

# The story begins here.
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

# In this part your given the chance to explore a little.
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

# In this part the player has the choice to pick up one of the three weapons presented to them
# and keep one as you primary weapon.
while gameState == 2.4:
    user_input = input("""
    You've run towards the screams to find a group of three masked assailants covered in
    blood wielding swords on the verge of attacking a mother and her child.
    
    There are three weapons in close proximity to you. A Sword, Spear, and Dagger.

    Which weapon do you pick up?
    
    \nPlayer Options: \n1) Sword\n2) Spear\n3) Dagger\n:""")

# Sword information
    if user_input.lower() == "sword":
        primaryWeapon1['Primary Weapon'] = 'Sword'
        primaryWeapon1['Attack One'] = 27
        primaryWeapon1['Attack Two'] = 18
        primaryWeapon1['Attack Three'] = 33
        print("""

        You have chosen the Sword as your primary weapon

        """)
        weaponCounter = 1
        gameState = 2.5

# Spear information
    if user_input.lower() == "spear":
        primaryWeapon1['Primary Weapon'] = 'Spear'
        primaryWeapon1['Attack One'] = 30
        primaryWeapon1['Attack Two'] = 22
        primaryWeapon1['Attack Three'] = 36
        print("""

        You have chosen the Spear as your primary weapon

        """)
        weaponCounter = 1
        gameState = 2.5

# Dagger information
    if user_input.lower() == "dagger":
        primaryWeapon1['Primary Weapon'] = 'dagger'
        primaryWeapon1['Attack One'] = 15
        primaryWeapon1['Attack Two'] = 11
        primaryWeapon1['Attack Three'] = 20
        print("""

        You have chosen the Dagger as your primary weapon

        """)
        weaponCounter = 1
        gameState = 2.5

# In this the part the player will begin their first fight.
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
    print("Murai")
    print(player1)
    print("\n")

    for key, value in primaryWeapon1.items():
        print(key, ':', value)
    gameState = 2.7
    break

# Fight One
while gameState == 2.7:

    user_input = input("""\nEnter Attack\n:""")

    for key in primaryWeapon1.items():
        if user_input.lower() == 'attack one':
            enemy1['Health'] = (enemy1.get('Health') - primaryWeapon1.get('Attack One'))
            player1['Health'] = (player1.get('Health') - 10)
            print("\n")
            print("Murai")
            print(player1)
            print("\n")
            print("Masked Assailant")
            print(enemy1)

        if user_input.lower() == 'attack two':
            enemy1['Health'] = (enemy1.get('Health') - primaryWeapon1.get('Attack Two'))
            player1['Health'] = (player1.get('Health') - 12)
            print("\n")
            print("Murai")
            print(player1)
            print("\n")
            print("Masked Assailant")
            print(enemy1)

        if user_input.lower() == 'attack three':
            enemy1['Health'] = (enemy1.get('Health') - primaryWeapon1.get('Attack Three'))
            player1['Health'] = (player1.get('Health') - 14)
            print("\n")
            print("Murai")
            print(player1)
            print("\n")
            print("Masked Assailant")
            print(enemy1)

        if enemy1['Health'] <= 0:
            player1['Exp'] = (player1.get('Exp') + enemy1.get('Exp'))
            print("\nYou've just received +10Exp\n")
            gameState = 3
        break
#The player is given the choice to capture of kill the masked assailant.
while gameState == 3:

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

# This will just inform the player on the decision they just made
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
    # The player will receive more Exp for interacting with the villagers
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
    
    You begin to think that it's another attack on the village but you hear from one of 
    the villagers that the hut where the masked assailant is in has been set on fire.

    \nPlayer Options: \n1) Help put the fire out\n:""")

    if user_input.lower() == "help put the fire out":
        gameState = 4.1

while gameState == 4.1:
    user_input = input("""
    You and few other villagers have put out the fire before it could spread even more.
    ...
    \nPlayer Options: \n1) Next\n:""")
    if user_input.lower() == "next":
        if hasKilled == 1:
            gameState = 7


while gameState == 5:
    user_input = input("""
                                        Day Two: I you captured the guy

    A beam of light hits your face waking you up, you take your time getting up today as 
    you think about... and you realise the smell of smoke is still in the air and... is 
    silent, the sounds of children playing outside isn't there anymore instead you can 
    hear the wind brush the ground and the 'Ka Kaw' of the crows as they feeding of the 
    ... remains.

    What do you do?

    \nPlayer Options: \n1) Get Up\n2) Lay in\n:""")

    if user_input.lower() == 'get up':
        gameState = 5.1

    if user_input.lower() == 'lay in':
        gameState = 5.2


while gameState == 5.1:
    user_input = input("""
    You get up and go outside to find out that the that the masked assailant was murdered
    whilst he slept.
    
    It could been anyone.
    
    The village's Old lady who lost he son as he protected her.
    
    The son who lost both his parent in a fire.
    
    or the numerous villagers who lost a family member that was in the... village guardians
    
    It could been anyone.
    
    \nPlayer Options: \n1) Go check on the masked assailant\n:""")

    if user_input.lower() == 'go check on the masked assailant':
        gameState = 7

while gameState == 5.2:
    user_input = input("""
    A Couple hours Later a village's old lady knocks on your door waking you up. 
    
    She tells you that the masked assailant was murdered during the night as you 
    were the one to chose to keep him alive. 

    \nPlayer Options: \n1) Go check on the Masked Assailant\n:""")

    if user_input.lower() == 'go check on the masked assailant':
        gameState = 7

# I you killed the guy
while gameState == 6:
    user_input = input("""
                                        Day Two:

    A beam of light hits your face waking you up, you take your time getting up today as 
    you think about... and you realise the smell of smoke is still in the air and... is 
    silent, the sounds of children playing outside isn't there anymore instead you can 
    hear the wind brush the ground and the 'Ka Kaw' of the crows as they feeding of the 
    ... remains.

    You begin to regret your decision when you chose to kill the only guy who could provide
    you with information on the group who massacred the village.
     
    With that in mind you begin to get curious about about those individuals who you kill
    and you get up and investigate their what remains of them.

    What do you do?

    \nPlayer Options: \n1) Get and Investigate\n:""")

    if user_input.lower() == 'get and investigate':
        gameState = 7

while gameState == 7:
    user_input = input("""
    You decide to investigate the bodies of the three masked individuals to find any information 
    on who they are and where they came from.

    \nPlayer Options: \n1) Next\n:""")

    if user_input.lower() == "next":
        gameState = 7.1

while gameState == 7.1:
    user_input = input("""
    
    Something shiny catches your eye.
    
    \nPlayer Options: \n1) Pick up and Inspect\n:""")

    if user_input.lower() == 'pick up and inspect':
        gameState = 7.2

while gameState == 7.2:
    user_input = input("""
    It's a silver medallion.
    
    you check to see if the other two have one. 
    
    And they do!
    
    You rub off the blood that stained the medallion to find insignia printed on it
    
    You recognise that insignia.
    
    It belongs to a clan of raiders...

    \nPlayer Options: \n1) Next\n:""")

    if user_input.lower() == 'next':
        gameState = 7.3

while gameState == 7.3:
    user_input = input("""
    After hours of dwelling on whether or not you should go after this group, your body
    gets the urge to get up and pack...You leave the village in pursuit of these
    
    \nPlayer Options: \n1) Next\n:""")

    if user_input.lower() == 'next':
        gameState = 7.4

while gameState == 7.4:
    user_input = input("""
    You've left the village and you've been walking for a while now there and now reached 
    a cross-road.
    
    There are three paths that you can take. 
    
       - The sandy path on the left. 
        
       - The Middle path full of greenery.
        
       - or the path on the right that seems like any ordinary path.
    
    Which path do you take?
    
    \nPlayer Options: \n1) Left\n2) Middle\n3) Right\n:""")

    if user_input.lower() == 'left':
        print("""
        \nYou have chosen the path on the left""")
        gameState = 8

    if user_input.lower() == 'middle':
        gameState = 8.5

    if user_input.lower() == 'right':
        gameState = 10

# Left path
while gameState == 8:
    user_input = input("""
    You have chosen the path on the left.
    
    On Your journey to hunt those individuals down you hear someone screaming for help.

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

    if user_input.lower() == 'make a loud noise':
        gameState = 8.

# The part Where you laugh the man and the bears mother laughs
while gameState == 8.2:
    user_input = input("""
    While your laughing at him you hear some rustling bushes to your left.

    It's the bears mother and it's twice the size of child

    She Claws at him, but  you get there in time to push him out of the way.

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
        print("\n+30 Health\n")

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
    user_input = input("""\nEnter Attack\n:""")

    for key in primaryWeapon1.items():
        if user_input.lower() == 'attack one':
            enemy2['Health'] = (enemy2.get('Health') - primaryWeapon1.get('Attack One'))
            player1['Health'] = (player1.get('Health') - 15)
            print("\n")
            print("Murai")
            print(player1)
            print("\n")
            print("Bear")
            print(enemy2)

        if user_input.lower() == 'attack two':
            enemy2['Health'] = (enemy2.get('Health') - primaryWeapon1.get('Attack Two'))
            player1['Health'] = (player1.get('Health') - 17)
            print("\n")
            print("Murai")
            print(player1)
            print("\n")
            print("Bear")
            print(enemy2)

        if user_input.lower() == 'attack three':
            enemy2['Health'] = (enemy2.get('Health') - primaryWeapon1.get('Attack Three'))
            player1['Health'] = (player1.get('Health') - 16)
            print("\n")
            print("Murai")
            print(player1)
            print("\n")
            print("Bear")
            print(enemy2)

        if enemy2['Health'] <= 0:
            gameState = 9.2
        break

# The part where you choose to scare away the bear instead of killing it.
# The player also gets more Exp if they chose to scare the bear away instead of kill it.
while gameState == 8.4:
    user_input = input("""
    The loud noise scares the bear away.

    \nPlayer Options: \n1) Next\n:""")

    if user_input.lower() == "next":
        player1['Exp'] = (player1.get('Exp') + enemy2.get('Exp'))
        print("\nYou've just received +50Exp\n")
        gameState = 9.2

# The player also receives a large healing item.
while gameState == 9.2:
    user_input = input("""
    The man thanks you for saving his life and he offers you an healing item for do so.

    Do you accept or decline
    \nPlayer Options: \n1) Accept\n2) Decline\n:""")

    if user_input.lower() == "accept":
        print("You've received a Healing Item\n")
        playerHealthItemBig['How Many'] = (playerHealthItemBig.get('How Many') + 1)
        print(playerHealthItemBig)
        gameState = 9.3

    if user_input.lower() == "decline":
        print("You've Decline the item\n")
        gameState = 9.3

while gameState == 9.3:
    user_input = input("""
    After a while of walking and talking... he finally introduces himself as Tim Allen the Bard.
    
    You've Told him what happen to your village and showed him the medallion with the 
    insignia.
    
    \nPlayer Options: \n1) Next\n:""")

    if user_input.lower() == 'next':
        gameState = 9.4

while gameState == 9.4:
    user_input = input("""
    He recognises the insignia and informs you that their currently basing their operations
    in a run down house north of your currently location.
    
    He ask 'do you really want to do this, your only one man'.
    
    With a determined look in your eye you reply with a firm 'YES'.
    
    He draws you a simple line map... that guids you to their current location.
    
    \nPlayer Options:\n1) Follow the map\n:""")

    if user_input.lower() == 'follow the map':
        gameState = 14


# Middle path
# the part of the Story When you talk to a Magic Tree
while gameState == 8.5:
    user_input = input("""
    You've been walking for a while and you notice that it's begging to get dark.
    
    There's a faint light in the distance and the closer you get the warmer it gets.
    
    What do you do?

    \nPlayer Options: \n1) Approach the light\n:""")

    if user_input.lower() == "approach the light":
        gameState = 8.6

while gameState == 8.6:
    user_input = input("""
    You approach the light to find a large tree. The light that you saw was the cluster
    of fire flies illuminating everything in close proximity.You take a seat at the foot 
    of the tree and you being to fall asleep. 
    
    You feel something brush your face.
    
    It's feels like a branch.
    
    
    \nPlayer Options: \n1) Wake up push the branch away.\n:""")

    if user_input.lower() == "wake up and push the branch away":
        gameState = 8.7

while gameState == 8.7:
    user_input = input("""
    The branch whacks you in the face this time.
    
    You get cut the branch and you hear something say 'ouch'.
    
    Another branch whacks you in the face.
    
    ...complete
    
    You finally realise that it's the tree speaking to you 

    \nPlayer Options: \n1)\n:""")

    if user_input.lower() == "":
        gameState = 8.9

while gameState == 8.9:
    user_input = input("""
    You begin to question your sanity and as you talk to the tree.
    
    The tree hits you again but this time it's different.
    
    You feel and see all the sadness, the pain, and all the destruction that was caused 
    that day.
    
    ...complete
 
    \nPlayer Options: \n1) Next\n:""")

    if user_input == "next":
        gameState = 8.10

while gameState == 8.10:
    user_input = input("""
    Speaking speaking Tree offers you a new weapon to aid you in your pursuit of the 
    group of raiders.
    
    Your offered The Grass Blade, a Wooden mace, Earth Gauntlets. 
    
    \nPlayer Options: \n1) Grass Blade\n2) Wooden Mace\n3) Earth Gauntlets\n:""")

# Grass Blade
    if user_input.lower() == "grass blade":
        secondaryWeapon1['Secondary Weapon'] = 'Grass Blade'
        secondaryWeapon1['Attack One'] = 27
        secondaryWeapon1['Attack Two'] = 18
        secondaryWeapon1['Attack Three'] = 33
        print("""
        You have chosen the Grass Blade as your secondary weapon

        """)
        weaponCounter = 2
        gameState = 8.11

# Wooden Mace
    if user_input.lower() == "wooden mace":
        secondaryWeapon1['Secondary Weapon'] = 'Wooden Mace'
        secondaryWeapon1['Attack One'] = 30
        secondaryWeapon1['Attack Two'] = 22
        secondaryWeapon1['Attack Three'] = 36
        print("""
        You have chosen the Wooden Mace as your secondary weapon

        """)
        weaponCounter = 2
        gameState = 8.11

# Earth Gauntlets
    if user_input.lower() == "earth gauntlets":
        secondaryWeapon1['Secondary Weapon'] = 'earth gauntlets'
        secondaryWeapon1['Attack One'] = 29
        secondaryWeapon1['Attack Two'] = 24
        secondaryWeapon1['Attack Three'] = 31
        print("""
        You have chosen the Earth Gauntlets as your secondary weapon

        """)
        weaponCounter = 2
        gameState = 8.11

while gameState == 8.11:
    user_input = input("""
    You wake up thinking that what all that happened last night was all a dream but 
    you find your self equipped with a new weapon.
    
    The sun is shining, the birds are chirping and as you get up a clear path opens up
    
    Boulders move to the side and a strong gust of wind pushes you forwards... 
    
    \nPlayer Options: \n1) Follow the path:""")

    if user_input.lower() == "follow the path":
        gameState == 14




# Right path

# while gameState == 10:
#     user_input = input("""
#     You have chosen the path on the right.
#
#     You've been walking for a while now and you noticed that it's begging to get
#     dark. In the distance you see faint light and you hear singing and laughter.
#
#     What do you do?
#
#     \nPlayer Options: \n1) Approach the group\n2) Scout them out\n:""")
#
#     if user_input.lower() == "approach the group":
#         gameState = 10.2
#
#     if user_input.lower() == "scout them out":
#         gameState = 10.1
#
# while gameState == 10.1:
#     user_input = input("""
#     You've chosen to be cautions and scout them out before you interact with them.
#
#     1) They look like a rough bunch of guys.
#     2) A Stack weapons covered in blood.
#     3) One of the men is wearing A mask similar to the men that you caught village.
#     4) You hear Another man bragging about what he did to your village.
#
#     The man wearing the mask walks away.
#
#     \nPlayer Options: \n1) Approach them\n2) Go after the man who just walked away\n:""")
#
#     if user_input.lower() == "approach them":
#         gameState = 10.2
#
#     if user_input.lower() == "go after the man who just walked away":
#         gameState = 10.00000
#
# while gameState == 10.2:
#     user_input = input("""
#     You've approach them and they all go silent. They all look and Stare at you for a
#     while before they ask you take a seat.
#
#     They offer you food, a drink, and the option to Stay the night.
#
#     Theres a lot of conversation going on... one of them asks you about your journey.
#
#     \nPlayer Options: \n1) Tell them the truth\n2) Lie about it\n:""")
#
#     if user_input.lower() == "tell them the truth":
#
#         if scouted == 1:
#             gameState = 11
#
#         if scouted == 2:
#             gameState = 11.1
#
#     if user_input.lower() == "lie about it":
#
#         if scouted == 2:
#             gameState = 12.3
#
#         if scouted == 1:
#             gameState = 12.4
#
# the path if you chose to tell the truth - approaching them without scouting them first
# while gameState == 11:
#     user_input = input("""
#     You have chosen to tell the truth.
#
#     You've told them that you've left your village in pursuit of a group of people.
#
#     They're all drunk, they think nothing of it and continue to laugh, sing, and drink
#     before they all call it a night.
#
#     Just as your about to go to sleep something catches your eye.
#
#     You see a mask that closely resembles the ones you found the masked assailants wearing.
#
#     You being to realise who these people really are.
#
#     What do you?
#
#     \nPlayer Options: \n1) Leave\n 2) Revenge\n:""")
#
#     if user_input.lower() == "leave":
#         print("\nYou've panicked and chosen to leave")
#         gameState = 11.2
#
#     if user_input.lower() == "revenge":
#         print("\nYou have chosen to take your revenge")
#         gameState = 11.2
#
# the path if you chose to tell the truth - approaching them after scouting them first
# while gameState == 11.1:
#     user_input = input("""
#     You have chosen to tell the truth while reminding your self that yor need to be
#     very cautions about this group.
#
#     You've told them that you've left your village in pursuit of a group of people.
#
#     They're all drunk, they think nothing of it and continue to laugh, sing, and drink
#     before they all call it a night.
#
#     Seeing the mask's on the floor confirms your suspicions
#
#     You begin to panic.
#
#     What do you?
#
#     \nPlayer Options: \n1) Leave\n 2) Revenge\n:""")
#
#     if user_input.lower() == "leave":
#         print("\nYou've panicked and chosen to leave")
#         gameState = 11.1
#
#     if user_input.lower() == "revenge":
#         print("\nYou have chosen to take your revenge")
#         gameState = 11.1
#
# if you lied but scouted them out before you joined them.
# while gameState == 12.3:
#     user_input = input("""
#     You've chosen to lie to them.
#
#     You've told them that you've been out on a hunting job for 2 days and your from
#     a village up north in the mountains.
#
#     They think nothing of it and continue to laugh, sing, and drink before they all call
#     it a night.
#
#     Knowing what you know what do you do?
#
#     \nPlayer Options: \n1) Leave\n 2) Revenge\n:""")
#
#     if user_input.lower() == "revenge":
#         gameState = 12.5
#
#     if user_input.lower() == "leave":
#         gameState = 12.6
#
# # if you lied to them but you didn't scout them out before joining them.
# while gameState == 12.4:
#     user_input = input("""
#     You've chosen to lie
#
#     You've told them that you've been out on a hunting job for 2 days and your from
#     a village up north in the mountains.
#
#     They think nothing of it and continue to laugh, sing, and drink before they all call
#     it a night.
#
#     \nPlayer Options: \n1) Leave\n 2) Sleep\n:""")
#
#     if user_input.lower() == "leave":
#         print("""
#     You've chosen to leave and as you leave something catches your eye, someone returns
#     to the camp wearing a very familiar mask
#
#     You've gotten up to follow this man.""")
#         gameState = 12.5
#
#     if user_input.lower() == "sleep":
#         print("""
#     You've chosen to stay the night. You hear some rustling, you realise that someone has
#     returns to the camp wearing a very familiar mask
#
#     You've gotten up to follow this man.""")
#         gameState = 12.5

# while gameState == 12.5:
#     user_input = input("""
#     You have chosen to lie.
#
#     Everyone's gotten tired and has fallen asleep...
#
#     \nPlayer Options: \n1) :""")
#
#     if user_input.lower() == "leave":
#         print("You have chosen to leave them alone")
#         gameState = 12.6
#
#     if user_input.lower() == "kill them while they sleep":
#         gameState = 12.6
#


# complete
# while gameState == 12.5:
#     user_input = input("""
#     You've chosen to take revenge...
#
#     \nPlayer Options: \n1) Option\n:""")
#
#     if user_input.lower() == "option":
#         gameState = 12.000


# the path if you chose to tell the truth - approaching them without scouting them first


# while gameState == 12.6:
#     user_input = input("""
#     You've chosen leave...
#
#     As your leaving You find the man that was wearing the mask by himself
#
#     \nPlayer Options: \n1) Knock him out\n:""")
#
#     if user_input.lower() == "knock him out":
#         print("After you've knocked him out and tied him to a tree you begin to questioning him")
#         gameState = 10.7

# Questioning part 1
# while gameState == 10.7:
#     print("""
#     The masked man says: """ + random.choice(enemyOneAnswers))
#     user_input = input("""
#     What do you ask?
#
#     \nPlayer Options: \n1) Do you know who I am?\n2) Do you know where i'm from?\n:""")
#
#     if user_input.lower() == "do you know who i am?":
#         pass
#
#     if user_input.lower() == "do you know where i'm from?":
#         print("""
#         The masked man begins to get aggressive and shouts for help. But nobody answers.
#         """)
#         gameState = 10.8
#
# # Questioning part 2
# while gameState == 10.8:
#     print("""
#     You tell him nobody's going to answer his cries for help and him only option is to
#     tell you where the rest of his group are currently hiding out.
#
#     The masked man says: """ + random.choice(enemyTwoAnswers))
#     user_input = input("""
#     What do you ask?
#
#     \nPlayer Options: \n1) Did you guys think you could really get away with it?\n2) Why did you do it?\n:""")
#
#     if user_input.lower() == "did you guys think you could really get away with it?":
#         pass
#
#     if user_input.lower() == "why did you do it?":
#         print("""
#         The masked man is beginning to get confused. You take his mask of to see the
#         man behind the mask.
#
#         His face is covered in scars and you notice that he's blind in one eye.""")
#         gameState = 10.9
#
# # Questioning part 3
# while gameState == 10.9:
#     print("""
#     You tell him that your from Ringo and the look on his face suddenly changes.
#
#     The masked man says: """ + random.choice(enemyThreeAnswers))
#     user_input = input("""
#     What do you ask?
#
#     \nPlayer Options: \n1) Point a knife at his only good eye\n2) Tell me where the rest of you are hiding out\n3) Complying is your best and only option\n:""")
#
#     if user_input.lower() == "complying is your best and only option":
#         pass
#
#     if user_input.lower() == "tell me where the rest of you are hiding out":
#         pass
#
#     if user_input.lower() == "point a knife at his only good eye":
#         print("""
#         The man begins to sweat as he turns his head away""")
#         gameState = 10.9
#
# # Questioning part 4
# while gameState == 10.10:
#     print("""
#     You warn him again promising that he'll lose his one and only working eye if he if he doesn't talk.
#
#     The masked man says: """ + random.choice(enemyFourAnswers))
#     user_input = input("""
#     What do you ask?
#
#     \nPlayer Options: \n1) \n2) \n3) \n:""")
#
#     if user_input.lower() == "":
#         pass
#
#     if user_input.lower() == "":
#         pass
#
#     if user_input.lower() == "":
#         print("""
#         """)
#         gameState = 10.11
#
# # Questioning part 5
# while gameState == 10.11:
#     print("""
#
#
#     The masked man says: """ + random.choice(enemyFourAnswers))
#     user_input = input("""
#     What do you ask?
#
#     \nPlayer Options: \n1) \n2) \n3) \n:""")
#
#     if user_input.lower() == "":
#         pass
#
#     if user_input.lower() == "":
#         pass
#
#     if user_input.lower() == "":
#         print("""
#         """)
#         gameState = 10.12
#
# # Questioning part 6
# while gameState == 10.12:
#     print("""
#
#
#     The masked man says: """ + random.choice(enemyFourAnswers))
#     user_input = input("""
#     What do you ask?
#
#     \nPlayer Options: \n1) \n2) \n3) \n:""")
#
#     if user_input.lower() == "":
#         pass
#
#     if user_input.lower() == "":
#         pass
#
#     if user_input.lower() == "":
#         print("""
#         """)
#         gameState = 10.13

while gameState == 14:
    user_input = input("""
    You've finally arrived at their hideout it doesnt seem as lively as you'd though it would be 
    The building is covered in moss, vines and mold. The house is practically fall apart.
    
    Your being to get nervous but revenge is the only thing on your mind.
    
    \nPlayer Options: \n1) Enter the building:""")

    if user_input.lower() == "enter the building":
        gameState = 14.1

while gameState == 14.1:
    user_input = input("""
    The air inside... Your presented with Three doors that with a
    
    Which Door do you enter?
    
    \nPlayer Options: \n1) Door 1\n2) Door 2\n3) Door 3\n:""")

    if user_input.lower() == "door 1":
        gameState = 14.2

    if user_input.lower() == "door 2":
        gameState = 14.3

    if user_input.lower() == "door 3":
        gameState = 14.4

while gameState == 14.2:
    user_input = input("""
    You've chosen to enter Door number one.
    
    This room looks like it's being used as a place to store inventory.
    
    Look around the room to see what you can find.
    
    \nPlayer Options: \n1) Look Around:""")

    if user_input.lower() == "look around":
        print("You've Found 4 Healing Item\n")
        playerHealthItemBig['How Many'] = (playerHealthItemBig.get('How Many') + 4)
        print(playerHealthItemBig)
        gameState =000
#       Next room

while gameState == 14.3:
    user_input = input("""
    You've chosen to enter Door number two.

    This room looks like it's being used to store and upgrade weaponry.

    Would you like to upgrade a weapon?

    \nPlayer Options: \n1) Yes\n2) No\n:""")

    if user_input.lower() == "Yes":
        if weaponCounter == 1:
            gameState = 14.4

    if user_input.lower() == "Yes":
        if weaponCounter == 2:
            gameState = 14.5

# If the player only has one weapon
while gameState == 14.4:
    user_input = input("""
    Upgrade your Primary Weapon.
    
    \nPlayer Options: \n1) Upgrade Primary Weapon""")

    if user_input.lower() == "upgrade primary weapon":
        primaryWeapon1['Attack One'] = (primaryWeapon1.get('Attack One') + 40)
        primaryWeapon1['Attack Two'] = (primaryWeapon1.get('Attack Two') + 40)
        primaryWeapon1['Attack Three'] = (primaryWeapon1.get('Attack Three') + 40)
        print("""
        You have chosen to Upgrade your primary weapon""")
        gameState = 000

# If the player two weapons
while gameState == 14.5:
    user_input = input("""
    Which weapon do you want to Upgrade.

    \nPlayer Options: \n1) Primary Weapon\n2) Secondary Weapon""")

    if user_input.lower() == "upgrade primary weapon":
        primaryWeapon1['Attack One'] = (primaryWeapon1.get('Attack One') + 40)
        primaryWeapon1['Attack Two'] = (primaryWeapon1.get('Attack Two') + 40)
        primaryWeapon1['Attack Three'] = (primaryWeapon1.get('Attack Three') + 40)
        gameState =000

    if user_input.lower() == "upgrade secondary weapon":
        secondaryWeapon1['Attack One'] = (secondaryWeapon1.get('Attack One') + 40)
        secondaryWeapon1['Attack Two'] = (secondaryWeapon1.get('Attack Two') + 40)
        secondaryWeapon1['Attack Three'] = (secondaryWeapon1.get('Attack Three') + 40)
        gameState =000


# while gameState == 00000:
#     user_input = input("""
#     There all asleep...
#     """)
#     if user_input = "":
#         gameState =000000
#
# while gameState == 00000:
#     user_input = input("""
#     You encuonter one for the maskmen
#     """)
#     if user_input = "":
#         gameState =0000000

















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
