list_arr = []
n = int(input("Enter the number of item on the list-:"))
for i in range(n):
    number = int(input("Enter the number-:"))
    list_arr.append(number)
    slist_arr = sorted(list_arr)
print("The number is:",slist_arr)

item = int(input("Enter the  number to search-:"))
def binarysearch(slist_arr, item):
    first = 0
    last = len(slist_arr)-1
    found = False 
    while first <= last and not found:
        midpoint = (first + last)//2
        
        if slist_arr[midpoint] == item:
            found =True
        else:
            if item < slist_arr[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1 
          
    return found
position = (binarysearch(slist_arr, item))
print(position)
for i in range(len(slist_arr)):
    if item == slist_arr[i]:
        print("The position of the number is:", i)
