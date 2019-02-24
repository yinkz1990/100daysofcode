def bubble_sort(sort_list):
    for num in range(len(sort_list)):
        for num1 in range(len(sort_list)-1):
            if sort_list[num1]>sort_list[num1+1]:
                sort_list[num1], sort_list[num1+1] = sort_list[num1+1], sort_list[num1]
    print(sort_list)

sort_list = []
size = int(input("Enter the size of the list-:"))
for i in range(size):
    unsort_list = int(input("Enter the the element: \t"))
    sort_list.append(unsort_list)
bubble_sort(sort_list)

