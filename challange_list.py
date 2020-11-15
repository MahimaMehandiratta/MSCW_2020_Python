numbers = []
num = 0
print("Enter values:(To stop enter -999)")
while num != -999 :
    num = int(input())
    if num != -999:
        numbers.append(num)

print("Even numbers in the numbers are:")
for num in numbers:
   if num % 2 == 0:
      print(num, end = " ")
print("\nOdd numbers in the numbers are:")
for num in numbers:
   if num % 2 != 0:
      print(num, end = " ")
print("\n")
numbers.sort()
print("Largest number in the numbers is:")
print(numbers[-1])
print("Smallest number in the numbers is:")
print(numbers[0])