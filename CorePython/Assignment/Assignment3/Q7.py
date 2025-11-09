# Write a program to check if user has entered correct userid and password. 
user = 'sania'
pas = 'sania@123'
uid = input('Enter correct userid = ')
upass = input('ENter correct password = ')
if(uid == user and upass == pas):
    print('Correct UserId and Password')
else:
    print('Incorrect UserId and Password')