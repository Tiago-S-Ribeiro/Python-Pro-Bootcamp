import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_options = [rock, paper, scissors]

play = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_options[play])

comp = random.randint(0,2)
print("Computer chose:")
print(game_options[comp])

if play == 0 and comp == 2:
  print("You win!")
elif comp == 0 and play == 2:
  print("You lose")
elif comp > play:
  print("You lose")
elif play > comp:
  print("You win!")
elif play == comp:
  print("Draw.")