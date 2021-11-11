from data import MENU, resources
from art import logo

power_on = True

def print_report():
  measures = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    "money": "$"
  }
  for key in resources:
    print(f"{key}: {resources[key]}{measures[key]}")
  print("\n")

def stock_is_available(type):
  for ingredient in MENU[type]["ingredients"]:
    if MENU[type]["ingredients"][ingredient] > resources[ingredient]:
      print(f"Sorry there is not enough {ingredient}\n")
      return False
  return True

def request_coins():
  print("\nPayment procedure\n-----------------")
  quarters = float("{:.2f}".format(int(input("How many quarters? "))*0.25))
  dimes = float("{:.2f}".format(int(input("How many dimes? "))*0.10))
  nickles = float("{:.2f}".format(int(input("How many nickles? "))*0.05))      
  pennies = float("{:.2f}".format(int(input("How many pennies? "))*0.01))

  return quarters + dimes + nickles + pennies

def deduct_machine_materials(type, money):
  resources["money"] += money
  for ingredient in MENU[type]["ingredients"]:
    resources[ingredient] -= MENU[type]["ingredients"][ingredient]

print(logo)

while power_on:
  user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
  
  if user_choice == "off":
    break
  elif user_choice == "report":
    print_report()
  elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
    
    if stock_is_available(user_choice):
      value_inserted = request_coins()
      price = MENU[user_choice]["cost"]
      
      if value_inserted >= price:
        deduct_machine_materials(user_choice, price)
        print(f"Here's your {user_choice}, enjoy it while it's hot! ☕️\n")
        if value_inserted > price:
          print(f"Here's your change: {'{:.2f}'.format(value_inserted - price, 2)}$.\n")
      else:
        print("Sorry that's not enough money. Money refunded.")

  else:
    print(f"'{user_choice}' is not a valid input. Try again.\n")