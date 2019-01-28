numb1 = 0
numb2 = 1
count = 0

num = int(input("Enter the number of series-:"))

if num <= 0:
    print("Enter a number greater than zero")
else:

    while count < num:
        print(numb1, end=",")
        numb3 = numb2 + numb1
        numb1 = numb2
        numb2 = numb3
        count +=1

    