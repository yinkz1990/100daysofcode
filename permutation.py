num_of_list = int(input("Enter the length of list-:"))
number_perm = []
for num in range(num_of_list):
    list_num = int(input("Enter the number in the list-:"))
    number_perm.append(list_num)
def permutation(number_perm):
    if len(number_perm) == 0:
         return []
    if len(number_perm) == 1:
        return [number_perm]
    next_list = []
    for i in range(len(number_perm)):
        m = number_perm[i]
        remlist = number_perm[:i] + number_perm[i+1:]
        for p in permutation(remlist):
            next_list.append([m] + p)
    return next_list
data = number_perm
for p in permutation(data):
    print(p)
        

