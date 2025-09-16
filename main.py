#Setting price
cost = 3.50
#Welcoming customer
name = input("Welcome to the smoothie shop! Whats your name? \n")
#Asking smoothies
amount = input(f"Hello {name}! How many smoothies would you like? Each smoothie costs £3.50.\n")
#Working out price
total = float(amount) * float(cost)
#cool cup
coolcup = input("Would you like a nice cup to keep? It costs £1.\n")
coolcup = coolcup.lower()
if coolcup == "yes" or coolcup == "sure" or coolcup == "y":
    total = total + 1
else:
    print("Very well then, suit yourself.")
  #Show price
print(f"Thank you, {name}. The total for today will be £{total}")
