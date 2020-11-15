import sys
import datetime
CurrentDate = datetime.date.today()

try:
    deadline = input("What is the deadline for the project? (dd/mm/yyyy) ")
    deadline = datetime.datetime.strptime(deadline, "%d/%m/%Y").date()
except:
    print("Enter the date in the format mentioned!!!!")
    sys.exit()

diff = deadline - CurrentDate
diff = diff.days
print("Days remaining to complete of project: "+ str(diff))
week = int(diff/7)
diff = int(diff%7)
print("This is equivalent to: " + str(week)+" weeks and "+str(diff)+" days.")
print("Thank you for using application!!")