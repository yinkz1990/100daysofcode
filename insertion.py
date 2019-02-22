number_list = int(input("Enter the number of element in the list-:"))
alist = []
for number in range(number_list):
    in_list = int(input("Enter the number on the list-:"))
    alist.append(in_list)

def sort_list(alist):
    for index in range(0, len(alist)):
        current = alist[index]
        position = index

        while position > 0 and alist[position-1] > current:
            alist[position] = alist[position-1]
            position -=1
        alist[position] = current
    return alist

print("The sorted list is :", sort_list(alist))