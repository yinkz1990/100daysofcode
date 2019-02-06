users=["user1", "user2", "user3", "user4"]

user1={}
user2={}
user3={}
user4={}

#input details for user1
print("welcome user1")
username=input("Enter your username -:")
password=input("Enter your password -:")
gender=input("Enter your gender -:")
state=input("Enter your state -:")
country=input("Enter your country -:")

user1["username"]=username
user1["password"]=password
user1["gender"]=gender
user1["state"]=state
user1["country"]=country

print("user1= " + str(user1))
#input details for user2
print("welcome user2")
username=input("Enter your username -:")
password=input("Enter your password -:")
gender=input("Enter your gender -:")
state=input("Enter your state -:")
country=input("Enter your country -:")

user2["username"]=username
user2["password"]=password
user2["gender"]=gender
user2["state"]=state
user2["country"]=country
print("user2= "+ str(user2))

#input details for user3
print("welcome user3")

username=input("Enter your username -:")
password=input("Enter your password -:")
gender=input("Enter your gender -:")
state=input("Enter your state -:")
country=input("Enter your country -:")

user3["username"]=username
user3["password"]=password
user3["gender"]=gender
user3["state"]=state
user3["country"]=country
print("user3= " + str(user3))

#input details for user 4
print("welcome user4")

username=input("Enter your username -:")
password=input("Enter your password -:")
gender=input("Enter your gender -:")
state=input("Enter your state -:")
country=input("Enter your country -:")

user4["username"]=username
user4["password"]=password
user4["gender"]=gender
user4["state"]=state
user4["country"]=country

print("user4= " + str(user4))

#output details for user1 

for question, responses in user1.items():
    username=user1["username"]
    password=user1["password"]
    gender=user1["gender"]
    state=user1["state"]
    country=user1["country"]
print("This are your details user1")
print("username : " + username)
print("password : "+ password)
print("gender :"+ gender)
print("state :"+ state)
print("country :" + country)

##output details for user1
for question, responses in user2.items():
    username=user2["username"]
    password=user2["password"]
    gender=user2["gender"]
    state=user2["state"]
    country=user2["country"]
print("This are your details user1")
print("username : " + username)
print("password : "+ password)
print("gender :"+ gender)
print("state :"+ state)
print("country :" + country)

##output details for user1
for question, responses in user3.items():
    username=user3["username"]
    password=user3["password"]
    gender=user3["gender"]
    state=user3["state"]
    country=user3["country"]
print("This are your details user1")
print("username : " + username)
print("password : "+ password)
print("gender :"+ gender)
print("state :"+ state)
print("country :" + country)

##output details for user1
for question, responses in user4.items():
    username=user4["username"]
    password=user4["password"]
    gender=user4["gender"]
    state=user4["state"]
    country=user4["country"]
print("This are your details user1")
print("username : " + username)
print("password : "+ password)
print("gender :"+ gender)
print("state :"+ state)
print("country :" + country)

    


        
