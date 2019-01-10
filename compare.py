import random
element_1=[]
element_2=[]
player_1=0
player_2=0

for i in range(5):
    element_1=random.randint(1,6)
    element_2=random.randint(1,6)
    
    player_1+=element_1
    player_2+=element_2

    print ("player 1 =", element_1)
    print ("player 2 =", element_2)
print("player 1 has", player_1, "points while player 2 has", player_2, "points" )    
if player_1 > player_2:
    print("The winner of the competiton is player 1 with", player_1 , "points")
elif player_1 < player_2:
    print("The winner of the competiton is player 2 with", player_2 , "points")
else:
    print("There is no winner between player 1 and player 2")
