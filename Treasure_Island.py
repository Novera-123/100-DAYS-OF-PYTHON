ascii_art = """
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""-._ ".   |
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
"""

print(ascii_art)
print("WELCOME TO THE TREASURE ISLAND \n YOUR MISSION IS TO FIND THE TREASURE")
direction= input("What direction would you choose? for left press l and for right press r\n").lower()
if direction == 'l':
    print("You've come to a lake. There is an island in the middle of the lake.")
    option =input("Type wait to wait for a boat.Type swim to swim across\n").lower()
    if option == 'wait':
        print("You arrived at the island unharmed.There is a house with 3 doors.")
        color= input("One red,one yellow and one blue. Which color do you choose?\n").lower()
        if color == 'red':
            print("burned by fire. Game is over")
        elif color == 'blue':
            print("Eaten by beasts. Game over")
        elif color == 'yellow':
            print(" CONGRATULATIONS!! You win.")


    else:
        print("Attacked by trout.Game over")

else:
    print("You fell into a whole . Your game is over")