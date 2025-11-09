# Enter number of students from user. For those many students accept marks of 5  
# subject marks from user and calculate percentage. Display all percentage and  
# average percentage of students.
stud = int(input('Enter a number of student : ',))
average = 0
for i in range(1,stud+1):
    print()
    obtained_marks = 0
    print(f'Informaton of student {i}')
    for j in range(1,6):
        mark = float(input(f'Enter marks of subject {j}: '))
        obtained_marks += mark
    percentage = obtained_marks/500 * 100
    print(f'Percentage is {percentage}')
    average = average + percentage
print(f'Average percentage is : {average/stud}')