age = int(input('Enter your age ='))
categories =['Child','Adolescence','Adult',' Senior Adult']
adult = ['Early','Middle','Late']

if age >= 0 and age <= 12:
    print('You are a',categories[0]) 
elif age >= 13 and age <=18:
    print('You are an' ,categories[1])
elif age >=19 and age <=59:
    print('You are an' ,categories[2])
    if age >=19 and age <=25:
        print(adult[0] , 'adulthood')
    elif age >=26 and age <= 35:
        print(adult[1], 'adulthood')
    else:
        print(adult[2], 'adulthood')

elif age >=60:
         print('You are a' ,categories[3])