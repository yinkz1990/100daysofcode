import random
network = int(input("Choose a network provider, 1. for Mtn, 2 for Glo, 3 for Airtel, 4 for Etislat : "))

if (network == 1):
    print("Welcome to Mtn service provider")
    for x in range(13):
        print (random.randrange(0, 10), end="")
elif (network==2):
    print("welcome to Glo service provider")
    for x in range(15):
        print(random.randrange(0, 10), end="")

elif (network ==3):
    print("welcome to Airtel service provider")
    for x in range(13):
        print(random.randrange(0, 10) , end="") 
elif (network ==4):
    print("welcome to Etisalat service provider")
    for x in range(16):
        print(random.randrange(0, 9), end="")
else:
    print("Your netwwork provider is not available")
     