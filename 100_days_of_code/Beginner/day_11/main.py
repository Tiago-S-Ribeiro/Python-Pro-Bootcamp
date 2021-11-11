from replit import clear
from art import logo

def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  return a / b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)
  continue_calculating = "y"

  num1 = float(input("What's the first number? "))
  for key in operations:
    print(key)
  while continue_calculating == "y":
    operation = input("Choose an operation. ")
    num2 = float(input("What's the next number? "))
    function = operations[operation]
    result = function(num1, num2)

    print(f"{num1} {operation} {num2} = {round(result,2)}")
  
    continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. ")
    if continue_calculating == "y":
      num1 = result
    else:
      clear()
      calculator()

calculator()