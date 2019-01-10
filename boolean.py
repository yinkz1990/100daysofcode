foods=['Amala','Fufu','Eba','Semo','Rice','Beans','Spaghetti','Noodles']
found= True
print("This is our menu list:")
for i in foods:
    print(i)

def searchfoods():
    for food in foods:
        pick_food=input("choose a food from the available list:")
        if pick_food in foods:
            return found
            
        else:
            return not found
print("Search :", searchfoods())
print("You can place your order now ")

