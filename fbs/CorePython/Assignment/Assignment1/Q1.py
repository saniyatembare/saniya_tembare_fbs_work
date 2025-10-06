#Take marks of 5 subject 
m1 = int(input('Enter Marks of subject 1 : '))
m2 = int(input('Enter Marks of subject 2 : '))
m3 = int(input('Enter Marks of subject 3 : '))
m4 = int(input('Enter Marks of subject 4 : '))
m5 = int(input('Enter Marks of subject 5 : '))

#perform operation
gain_marks = m1+m2+m3+m4+m5
percentage = (gain_marks/500)*100

#display result
print(f'Percentage of the student is {percentage}%.')