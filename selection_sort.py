number_array = int(input("Enter the length of the array -: "))  
unsort_list=[]
for i in range(number_array):
    arr_list = int(input("Enter the array in the list-: "))
    unsort_list.append(arr_list)
def sort_selection(unsort_list):
    for i in range(0, len(unsort_list)-1):
        smallest = i
        for j in range(i+1, len(unsort_list)):
            if unsort_list[j] < unsort_list[smallest]:
                smallest = j
        unsort_list[i], unsort_list[smallest] = unsort_list[smallest], unsort_list[i]

sort_selection(unsort_list)
print("Sorted list : " , unsort_list)

