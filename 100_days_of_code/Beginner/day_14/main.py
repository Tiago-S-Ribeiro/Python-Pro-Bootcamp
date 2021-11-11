import random
from replit import clear
from art import logo, vs
from game_data import data

SIZE = len(data)
score = 0
game_over = False

compare_A = data[random.randint(0,SIZE)]    
data.remove(compare_A)                      
compare_B = data[random.randint(0,SIZE-1)]  
data.append(compare_A)                      
print(logo)

def cleanup():
  clear()
  print(logo)

while not game_over:
  
  if score > 0:  
    compare_A = compare_B                      
    data.remove(compare_A)                    
    compare_B = data[random.randint(0,SIZE-1)] 
    data.append(compare_A)                      

  print(f"A: {compare_A['name']}, a {compare_A['description']} from {compare_A['country']}.") 
  print(vs)
  print(f"B: {compare_B['name']}, a {compare_B['description']} from {compare_B['country']}.")

  user_choice = input("Who has more followers? Type 'A' or 'B'. ").lower()

  if compare_B['follower_count'] > compare_A['follower_count'] and user_choice == 'b':
    score += 1
    cleanup()
    print(f"You're right! Current score: {score}.\n")
  elif compare_A['follower_count'] > compare_B['follower_count'] and user_choice == 'a':
    score += 1
    cleanup()
    print(f"You're right! Current score: {score}.\n")
  else:
    game_over = True
  
cleanup() 
print(f"Wrong answer. Your final score: {score}.")