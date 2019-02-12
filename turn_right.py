num = []
n = int(input("Enter the num of item on the list-:"))
for i in range(n):
    number = int(input("Enter the number-:"))
    num.append(number)
print(num)

d = int(input("Enter the number of rotation-:"))
def rotate(num):
    if n >= 1 and n <= 10*5:
        if d >= 1 and d <= n:
            if len(num) >= 1 and len(num) <= 10*6:
                turn = num[d:] + num[:d]
                return turn
print("The turned number is :", rotate(num))
                
