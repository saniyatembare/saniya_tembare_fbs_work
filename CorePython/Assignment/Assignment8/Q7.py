# Write a program to find sum of digits of a number.

def sumDigit():
    num = int(input('Enter a number to print sum of digit : '))
    n = num
    sum = 0
    while(n != 0):
        d = n % 10
        n = n // 10
        sum += d
    print(sum)
sumDigit()