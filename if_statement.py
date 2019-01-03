number = int(input("Enter the number = "))

if number < 0:
    print(number,  "is a negative integer")
else:
    print(number,  "is a positive integer")

if number % 2:
    print(number,  "is an odd integer")
else:
    print(number, "is an even integer")