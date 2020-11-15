print("This program will open a file and read its content")
FileName = input("Enter the file name that you want to open.")
print("\n")
try:
    MyFile = open(FileName,'r')
    for value in MyFile:
        print(value)

except FileNotFoundError:
    print("The file does not exist.")


finally:
    print("Thank you for using the application!!!!")