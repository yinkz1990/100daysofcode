foods=['Amala','Fufu','Eba','Semo','Rice','Beans','Spaghetti','Noodles']
found= True
print("This is our menu list:")
for i in foods:
    print(i)

def searchfoods():
    for food in foods:
        pick_food=input("choose a food from the available list:").title()
        if pick_food in foods:
            found = True
            print(found)
            print("You can place your order now ")
    
        else:
            found = False
            print(found)
            print("Your food is not on our menu list")
print("Search :", searchfoods())

