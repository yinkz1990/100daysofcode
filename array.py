import array as arr
a=[5,8,9,75,45,32,7,8]
b=[46,7,23,12,7,10,17,9]
c=[15,9,23,42,31,25,12,15]
a_array= arr.array('i', a)
b_array= arr.array('i', b)
c_array= arr.array('i', c)
min_a= min(a_array)
min_b= min(b_array)
min_c= min(c_array)
max_a= max(a_array)
max_b= max(b_array)
max_c= max(c_array)
number= a_array + b_array
max_number=max(number)
l=sorted(number, reverse=True)
k=sorted(number, reverse=False)
i=[a_array + b_array for a_array,b_array in zip(a_array,b_array)]

print("This is a",a_array)
print("This is b",b_array)
print("This is c",c_array)
print("This is the combined array of a and b",number)
print("The minimum value of a array =", min_a)
print("The minimum value of b array =", min_b)
print("The minimum value of c array =",min_c)
print("The maximum value of a array =",max_a)
print("The maximum value of b array =",max_b)
print("The maximum value of c array =",max_c)
print("the maximun number for the combine array is",max_number)
print("The combined array a and b in descending order is :", l)
print("The combined array a and b in ascending order is :", k)
print(i)