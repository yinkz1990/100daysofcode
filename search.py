list_num = []
num = int(input("Enter the number of input -:"))

for n in range(num):
    numbers = int(input("Enter the number-:"))
    list_num.append(numbers)
print(list_num)
x = int(input("Enter the number to search -:"))
found = True
for i in range(len(list_num)):
    if  x == list_num[i]:
        found = True
        print(found)
        print("The position of the number is", i)
        break
else:
    found = False
    print("The number is not on the list above")
    





        



