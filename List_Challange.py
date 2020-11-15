print("Welcome to the application!")
guests = []
name = " "
print("Enter names of guest.(To stop enter #)")
while name != "#":
    name = str(input())
    if name != "#":
        guests.append(name.upper())
guests.sort()
print("-----------NAMES OF THE GUESTS IN ALPHABETICAL ORDER-----------")
for guest in guests:
    print(guest)