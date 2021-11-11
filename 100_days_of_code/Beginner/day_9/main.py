from replit import clear
#HINT: You can call clear() to clear the output in the console.
more_bidders = "yes"
bidders_list = {}

while more_bidders != "no": 
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  clear()
  bidders_list[name] = bid
max_val = max(bidders_list.values())
print(f"The winner is {max(bidders_list, key=bidders_list.get)} with a bid of ${max_val}.")