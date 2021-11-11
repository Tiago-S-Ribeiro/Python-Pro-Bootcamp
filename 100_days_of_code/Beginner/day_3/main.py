
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("wanna go 'left' or 'right'? ").lower()

if direction == "left":
  swim = input("there's a flood. 'wait' or 'swim' across the river? ").lower()
  if swim == "wait":
    color = input("3 doors. 'red', 'blue', or 'yellow'. Which one do you pick? ").lower()
    if color == "red":
      print("Burned by fire. Game Over.")
    elif color == "blue":
      print("Eaten by beasts. Game Over")
    elif color == "yellow":
      print("Gz. You won!")
    else:
      print("Game Over.")
  else:
    print("Trout attack. Game Over.")
else:
  print("You fall into a hole. Game Over.")