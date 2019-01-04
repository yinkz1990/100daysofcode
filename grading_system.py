score = int(input("Enter your grade point = "))
grade = ['A','B','C','D','E','F']

if score >=0 and score <= 39:
    print(grade[5])
if score < 0:
   print("grade cannot be ascribe to", score , "." + "Enter grade between 0 and 100")
elif score >=40 and score <= 44:
    print(grade[4])
elif score >=45 and score <=49:
    print(grade[3])
elif score >=50 and scores <=59:
    print(grade[2])

elif score >= 60 and scores <=69:
    print(grade[1])
elif score >= 70 and scores <=100:
    print(grade[0])







 
