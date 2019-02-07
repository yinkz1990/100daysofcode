def leap(year):
    found = True
    if year >= 1990 and year <= 10**5:
        if year % 400 == 0:
            return found
        if year % 100 == 0:
            return not found
        if year % 4 == 0:
            return found
        
        else:
            return not found
year = int(input("Enter the year-:"))

print(leap(year))

       

