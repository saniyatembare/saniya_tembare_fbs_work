# Write a program to check if entered number is a palindrome or 
# not. 

def palindrome_number(num):
    num1 = num
    digit = 0
    while(num1 != 0):
        d = num1 % 10
        num1 = num1 // 10
        digit = digit * 10 + d
    if(digit == num):
        return True  

n = int(input('Enter a numver : '))
result = palindrome_number(n)
if(result == True):
    print(f'{n} is palindrome')
else:
    print(f'{n} is not palindrome')
