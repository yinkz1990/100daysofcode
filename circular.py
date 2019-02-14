num = []
n = int(input("Enter the number of item on the list-:"))
for i in range(n):
    number = int(input("Enter the number-:"))
    num.append(number)
print("The number is:",num)

d = int(input("Enter the number of rotation-:"))
x = len(num) 

def rotate(num):  
    if n >= 1 and n <= 10*5:
        if d >= 1 and d <= 10*5:
            turn = num[-d:] + num[:-d]
            return turn
received = rotate(num)
print("Result of rotation is:",received)

for x in range(d):
    if len(received) >= 1 and len(received) <= 10*5:
        print(received[x+1], sep = "\n")
    
    


                