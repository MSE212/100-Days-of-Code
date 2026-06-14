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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
print("You find yourself on a deserted jungle trying to find your way to the island on the ocean.")

direction = input("What direction are you going? Left or Right? ").lower()

if direction == "left":
    print("You find yourself at the shore of a beach and when you spot an island far into the ocean.")
    transport = input("Will you swim there or use the boat? ").lower()

    if transport == "boat":
        print("After riding the boat for quite some time, you make it to the island.")
        print("Upon your arrival you encounter 3 doors, one Red, one Blue and one Yellow.")
        door = input("Which door will you choose? ").lower()

        if door == "yellow":
            print("Congratulations! You found the treasure.")
        elif door == "red":
            print("Too bad, you find the pits of hell and get consumed by your greed. Game Over.")
        elif door == "blue":
            print("Too bad, you find the outer space and get sucked into a vacuum, your organs explode and your blood boils instantly. Game Over.")
        else:
            print("Please type a valid answer.")
            
    elif transport == "swim":
        print("You decided that swimming was faster but after some time you start feeling exhausted until you drown. Game Over.")
    else:
        print("Please type a valid answer.")

elif direction == "right":
    print("Too bad, you encounter a tribe of hungry cannibals. Game Over")
else:
    print("Please type a valid answer.")
