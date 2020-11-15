print("This program calculates the charge for an order from an online store in Canada")
amt = float(input("Please enter you order total: $"))
country = input("Please enter the country: ")
country = country.lower()

if country == "canada":
    province = input("Enter the province: ")
    province = province.lower()
    if province == "alberta":
        amt += amt*(5/100)
        print("Total charge is $ "+ str(amt)+ " including 5% General Sales Tax.")
    elif province == "ontario":
        amt += amt*(13/100)
        print("Total charge is $ " + str(amt) + " including 13% Harmonized Sales Tax.")
    else:
        amt += amt*(11/100)
        print("Total charge is $ " + str(amt) + " including 6% Provisional Sales Tax and 5% General Sales Tax.")
else:
    print("There is no tax involved. Total charge is $ "+str(amt))