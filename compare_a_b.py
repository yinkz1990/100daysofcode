array_a=[]
array_b=[]
for i in range(3):
    a = float(input("Enter the number :"))
    b = float(input("Enter the number :"))
    c = array_a.append(a)
    d = array_b.append(b)
        
print(array_a)
print(array_b)

res1= [i for i,j in zip(array_a, array_b) if i > j]
res2= [i for i,j in zip(array_a, array_b) if j > i]
result_a = len(res1)
result_b = len(res2)
print([result_a, result_b])

   