# print treasure graphic
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# print story
print("Welcome to Treausre Island.")
print("Your mission is to find the treasure.")
# get input from user
# Use single and double quotes together ' "meep" '
# Escape the double quotes within the string (which is what im using below)
# Use triple-quoted strings: """ meep """"
# for clarification so type " < this one is ending the quote for type   > is the start of the left string "\"left\"" < escapes the left string
# /n can be used to go to the next line

direction = input("You're at a cross road. Where do you want to go Type " "\"left\"" " or " "\"right\" \n").lower()
if direction == 'right':
    print("You fell into a hole.\nGame Over.")
elif direction == 'left':
   cross = input("You come to a lake. There is an island in the middle of the lake. Type " "\"wait\"" " to wait for a boat. Type " "\"swim\"" " to swim across. \n").lower()
else:
    print("You fell into a hole.\nGame Over.")

if cross == 'wait':
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
elif cross == 'swim':
    print("You jump into the water to swim to the island but were attacked by a hungry trout. \nGame Over.")
else:
    print("You were attacked by a hungry trout. \nGame Over.")

if door == 'yellow':
    print("You opened the door to see...... \nA chest! You found the Treasure!")
elif door == 'blue':
    print("You opened the door to see...... \nA group of hungry Beasts! Game Over.")
elif door == 'red':
    print("You opened the door to see...... \nA lit fire, you walk closer and it splatters on you. \nGame Over.")
else:
    print("You didn't choose a door :( you die of boredom.\nGame over. )")
    
    