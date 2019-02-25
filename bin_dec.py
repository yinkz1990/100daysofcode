binary_number = int(input("Enter a binary number-:"))
print(binary_number)
def binary_dec(binary_number):
    i = 0
    decimal = 0
    while binary_number!=0:
        dec = binary_number % 10
        decimal = decimal + (dec*(2**i))
        binary_number = binary_number // 10
        i +=1
    print(decimal)
binary_dec(binary_number)
