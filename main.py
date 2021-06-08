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
crossroad = input("You are at a crossroad. Where do you want to go ? (Left or Right):\n ")
lower_crossroad = crossroad.lower()
if lower_crossroad == "left" :
  print("You are safe !!\n")
  swim = input("You have reached a lake.There is an island in the middle of the lake. Do you swim across the lake or wait for a boat?: \n")
  lower_swim = swim.lower()
  if lower_swim == "wait":
    print("You got lucky\n")
    door = input("You have arrived at a mansion unharmed. There are three doors in front of you. A red, a blue and a yellow. Which one do you choose?: \n")
    lower_door = door.lower()
    if lower_door == "red":
      print("Burned by fire. Game over.\n")
    elif lower_door == "blue":
      print("Eaten by beasts. Game over.\n")
    elif lower_door == 'yellow':
      print("Congrats !! U Win.\n")
    else:
      print("Game over\n")
  else:
    print("Oops !! Attacked by trout. Game over.\n")
else:
  print("Oops!! You fell into a hole. Game over.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload