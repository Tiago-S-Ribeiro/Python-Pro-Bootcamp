import random
import words
word_list = ["aardvark", "baboon", "camel"]
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(words.word_list)
display = []
game_over = False
lives = 6
flag = False

for i in chosen_word:
  display.append('_')

while not game_over:
  flag = False
  guess = input("\nGuess a letter:\n").lower()
  
  for i in range(0, len(chosen_word)): 
    if chosen_word[i] == guess:        
      display[i] = guess               
      flag = True
  if flag == False:
    lives -= 1
    print(f"\nYou missed. '{guess}' is not part of the word. You have {lives} tries left.")
    print(stages[lives])
  elif guess in display:
    print("\nYou already chose that option.")

  print(display)

  if "_" not in display and lives > 0:
    game_over = True
    print("You win.\n")
  if lives == 0:
    game_over = True
    print("You lose.\n")