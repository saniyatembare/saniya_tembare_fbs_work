# WAP to check if a given number is Armstrong number or not. For 
# each task create separate functions.

def armstrong_num(n1,p):
    n = n1
    sum = 1
    amt = 0
    while(n != 0):
        d = n % 10
        n = n // 10
        sum = d**p
        amt = amt + sum
    if(amt == n1):
        return True

num = int(input('Enter a number : '))
power = int(input('Enter a number ex 3 digit or 4 digit : '))
result = armstrong_num(num,power)
if(result == True):
    print(f'{num} is Armstrong')
else:
    print(f'{num} is not Armstrong')

