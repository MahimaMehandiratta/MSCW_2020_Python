import csv
filename = "GuestList.txt"
accessMode = 'r'
with open(filename, accessMode) as mycsvfile:
    dataFromFile = csv.reader(mycsvfile, delimiter =",")
    for row in dataFromFile:
        for value in row:
            print(value)