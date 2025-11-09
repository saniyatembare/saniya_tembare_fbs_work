num = int(input('Enter a number to check Number is palindrome or not : '))
n = num
d1 = n % 10
n = n // 10

d2 = n % 10
n = n // 10

d3 = n % 10
n = n // 10

if(d1 == d3):
    print('Number is palindrome')
else : 
    print('No is not palindrome')