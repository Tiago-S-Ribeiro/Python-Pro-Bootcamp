from replit import clear
import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  return random.choice(cards)

def calculate_score(list_of_cards):
  if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
    return 0
  if 11 in list_of_cards and sum(list_of_cards) > 21:
    list_of_cards.remove(11)
    list_of_cards.append(1)
  return sum(list_of_cards)

def compare(user, comp):
  if (user > 21 and comp > 21) or (user > 21):
    return "❌ You busted. You lose.\n"
  elif user == comp:
    return "♠️ ♦️ It's a draw ♥️ ♣️\n"
  elif comp == 0:
    return "❌ You lose. Opponent has a Blackjack.\n"
  elif user == 0:
    return "✅ You win with a Blackjack.\n"
  elif (user > comp) or (comp > 21):
    return "✅ You win!\n"
  else:
    return "❌ You lose.\n"
#---------------------------------------------------------
def play():
  user_cards = []
  comp_cards = []
  game_over = False
  print(logo)

  #deals initial cards
  for i in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())

  while not game_over:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}.")
    print(f"  Computer's first card: {comp_cards[0]}.")

    if user_score == 0 or comp_score == 0 or user_score > 21 or comp_score > 21:
      game_over = True
    else:
      hit = input("Type 'y' to get another card or 'n' to stand. ")
      if hit == "y":
        user_cards.append(deal_card())
      else:
        game_over = True

  while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_card())
    comp_score = calculate_score(comp_cards)

  print(f"\n Your final hand: {user_cards}, final score: {user_score}")
  print(f" Computer's final hand: {comp_cards}, final score: {comp_score}")
  print(compare(user_score, comp_score))

player_wishes_to_play = True

while player_wishes_to_play:
  user_wish = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if user_wish != "y":
    player_wishes_to_play = False
  else:
    clear()
    play()