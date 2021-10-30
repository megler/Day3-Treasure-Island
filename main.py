# treasureIsland.py
#
# Python Bootcamp Day 3 - Treasure Island
# Usage:
#      Easy Choose Your Own Adventure Game
#
# Marceia Egler Sept 23, 2021



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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input("Do you want to go left or right?").lower()

if direction == "left":
  motion = input("You walk for a little ways and come to a large lake. Do you want to swim or wait?").lower()

  if motion == "wait":
    door = input("After a few minutes, a boat appears. You get in and are taken across the lake to an islane. On the island is a cave with 3 doors. A red, a yellow and a blue. Which one do you want to open?").lower()
    if door == "yellow":
      print("Hooray! You found the treasure! You can now afford beer at the pub!")
    elif door == "blue":
      print("Awww...that was a bad life choice. The killer chihuahua ate you. Game over.")
    elif door == "red":
      print("Dude. You got toasted by a dragon. Game over.")
    else:
      print("You make horrible choices.  You didn\'t even pick the right door. Game over.")
  else:
    print("A sea otter ate your ass. Dummy. You should have waited. Game over.")
    
else:
  print("There are dragons and orcs to the right. Dummy. You should have gone left. Game over.")








