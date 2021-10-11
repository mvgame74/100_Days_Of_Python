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

first_choice = input("You are walking down a path in a dark, sinister forest... you find a fork in the way... you go left or right? ")
if first_choice.capitalize() == "Left":
  second_choice = input("You are going down the path until you reach a river... do you wait or swim? ")
  if second_choice.capitalize() == "Wait":
    third_choice = input("You arrive to an imposing building with three doors... which one would you chose: Red, Blue or Yellow? ")
    if third_choice.capitalize() == "Yellow":
      print("Congratulations, you found the treasure, married the princess and lived happily ever after!!!")
    elif third_choice.capitalize() == "Blue":
      print("You become a soldier and die protecting the royal family. Game Over.")
    elif third_choice.capitalize() == "Red":
      print("You become a servant and die cleaning the shit of the royal family. Game Over.")
    else:
      print("Duh! That wasn't even a choice. Game Over.")
  else:
    print("Wild piranhas attack and devour you. Game Over.")
else:
  print("You are attacked by bandits. Game Over.")

  


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload