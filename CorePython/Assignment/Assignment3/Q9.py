# Input 5 subject marks from user and display grade(eg.First class,Second class)
m1 = int(input('Enter marks of subject 1 : '))
m2 = int(input('Enter marks of subject 2 : '))
m3 = int(input('Enter marks of subject 3 : '))
m4 = int(input('Enter marks of subject 4 : '))
m5 = int(input('Enter marks of subject 5 : '))
 
Total = m1 + m2 + m3 + m4 + m5

percentage  = Total/500 * 100

if(percentage >= 90):
    print('Distinction')
elif(percentage >= 70):
    print('First class')
elif(percentage >= 60):
    print('Secound class')
elif(percentage >= 50):
    print('Pass class')
else:
    print('Fail')