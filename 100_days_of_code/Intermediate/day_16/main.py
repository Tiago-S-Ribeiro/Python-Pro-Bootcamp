from menu import Menu
from art import logo
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

print(logo)

while True:
  user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()

  if user_choice == "off":
    break
  elif user_choice == "report":
    coffee_maker.report()
    money_machine.report()
  elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
    drink = menu.find_drink(user_choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
      coffee_maker.make_coffee(drink)
  else:
    print(f"'{user_choice}' is not a valid input. Try again.\n")