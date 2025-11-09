# Write a program to prompt user to enter userid and password. After verifying 
# userid and password display a 4 digit random number and ask user to enter the 
# same. If user enters the same number then show him success message otherwise 
# failed. (Something like captcha) 
import random

userid = input('Enter userid : ')
password = input('Enter password : ')

captcha = random.randint(1111,9999)
print(captcha)

cap = int(input('Enter the correct captcha : '))
if(captcha == cap):
    print('Successfully Complete')
else:
    print('failed to complete')