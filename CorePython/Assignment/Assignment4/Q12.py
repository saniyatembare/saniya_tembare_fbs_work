# WAP to print Armstrong number within a given range
num = int(input('Enter a number to print armstrong number : '))
num_digit = int(input('Enter number 3 digit or 4 digit : '))
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