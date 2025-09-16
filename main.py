#Setting cost
cost = 3.50
#Welcoming customer
name = input("Welcome to the smoothie shop! Whats your name? \n")
#Asking how many smoothies they would like
amount = input(f"Hello {name}! How many smoothies would you like? Each smoothie costs £3.50.\n")
#Converting all numbers to float and calculating total cost
total = float(amount) * float(cost)
#Outputting customers final smoothie cost
print(f"Thank you, {name}. The total for your {amount} smoothie(s) will be {total}")
