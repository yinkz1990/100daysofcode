import random
fifa = ['10', '17', '7', '14', '12', '8', '15', '30']
print("The array below show the jersey number of players selected for Balloon D' or Award :" )
for number in fifa:
    print(number)
print("And the winner of the Balloon D' or is jersey number:", random.choice(fifa))
