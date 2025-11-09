# Write a program to check if given number is Armstrong number or not.  
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +  
# 4*4*4*4) 

num = int(input('Enter a number to print armstrong number : '))
num_digit = int(input('Enter number position ex 3 digit or 4 digit : '))
n = num
sum = 1
amt = 0
while(n != 0):
    d = n % 10
    n = n // 10
    sum = d**num_digit
    amt = amt + sum
if(num == amt):
    print(f'{num} is armstrong')
else:
    print(f'{num} is not armstrong')