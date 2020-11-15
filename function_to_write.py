def WriteToFile(FileName, Text):
    f = open(FileName,"a+")
    if Text != "#":
        f.writelines(Text + "\n")
    f.close()

FileName = input("Enter the file name you want to append: ")
print("Enter the the content (if you are done, Enter '#'):")
Text = " "
while Text != "#":
    Text = input()
    WriteToFile(FileName, Text)

