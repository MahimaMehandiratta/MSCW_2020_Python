print("This program will calculate your loan!!!!")
L = float(input("Enter the cost of loan: $"))
i = float(input("Enter the rate of interest in percentage: "))
n = float(input("Enter the number of years for loan: "))
i=i/100

M = L*(i*(1+i)*n)/((1+i)*n-1)
print("Your monthly payment is: ${0:.2f}".format(M))