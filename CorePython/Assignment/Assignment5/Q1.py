# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

Id = 'sania'
Pass = 'sania@123'

for i in range(1,4):
    id = input('Enter your Id : ')
    pas = input('Enter correct password : ')
    if(Id == id and Pass == pas):
        print('Correct Id and Password')
        break
    else:
        print('Incorrect Id and Password')
else:
    print('Card blocked')