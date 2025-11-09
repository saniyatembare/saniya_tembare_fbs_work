# Write a program find reverse of a number 

def revNumber():
    num = int(input('Enter a number to reverse : '))
    n = num
    rev = 0
    while(n != 0):
        d = n % 10
        n = n // 10
        rev = rev * 10 + d
    print(f'Reverse of the {num} is : {rev}')
revNumber()
