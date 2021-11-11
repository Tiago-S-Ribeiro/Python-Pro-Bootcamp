#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percent = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
num_people = int(input("How many people to split the bill? "))

#THIS WAY:

#tip_percentage = percent / 100 
#total_tip = total_bill * tip_percentage 
#final_amount = total_bill + total_tip
#each_person = final_amount / num_people
#final_each = round(each_person,2)
#print(f"Each person should pay {final_each}")

# OR SIMPLY:

final = "{:.2f}".format( (total_bill/num_people) * (1 +(percent/100)) )
#rounded = "{:.2f}".format(final)
print(f"Each person should pay: ${str(final)}")