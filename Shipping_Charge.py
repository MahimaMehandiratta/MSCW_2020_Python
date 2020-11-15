print("This program will calculate shipping charge!!!!!")
amt = float(input("Please enter the amount of your total purchase: $ "))

if amt < 50:
    amt += 10
    print("Shipping charge is ${0:.2f}".format(10))
    print("Total amount after adding shipping charges is ${0:.2f}".format(amt))
else:
    print("There is no shipping charge.")
    print("Total amount is ${0:.2f}".format(amt))
