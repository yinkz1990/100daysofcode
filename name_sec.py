if __name__ == '__main__':
    python_students = []
    for _ in range(int(input("Enter the value of n:"))):
        name = input("Your name:")
        score = float(input("Your score:"))
        python_students.append([score, name])
python_students.sort()
print(python_students)
temp = min(python_students)
capture = []
for i in range(len(python_students)):
    if python_students[i]==temp:
        capture.append(python_students[i+1])
    if python_students[i]==temp:
        capture.append(python_students[i+2])
capture_2=[]
for i in capture:
    for j in i:
        capture_2.append(j)
print(capture_2[1])
print(capture_2[3])
    

