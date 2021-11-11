from art import logo
import random

lives = 0
game_over = False

print(logo)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

random_num = random.randint(1,100)

if difficulty == "easy":
  lives = 10
  print("You have 10 attempts.")
else:
  lives = 5
  print("You have 5 attempts.")

while lives > 0 and not game_over:
  guess = input("Make a guess: ")
  if int(guess) > random_num:
    print("Too high 🔺")
    lives -= 1
    print(f"{lives} attempts left ⏳")
  elif int(guess) < random_num:
    print("Too low 🔻")
    lives -= 1
    print(f"✴️ No more tries left. The number was: [{random_num}]") if lives == 0 else print(f"{lives} attempts left ⏳")
  elif int(guess) == random_num:
    print(f"You got it. The answer was indeed {random_num} 🎉")
    game_over = True
