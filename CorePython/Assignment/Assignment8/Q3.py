# Write a program to find sum of following series using functions : 
# a.  1+ 2 + 3 + 4+….. + n 
# b. 1!+ 2! + 3! + 4!+….. + n! 
# c. 1^1 + 2^2 + 3^3+ …… n^n 
def sumSeries(sum):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
n = int(input('Enter a number to print sum : '))
result = sumSeries(n)
print(f'Sum of the series is : {result}','\n')

def multSeries(mult):
    mult = 1
    for i in range(1,num+1):
        mult *= i
    return mult
num = int(input('Enter a number to print a factorial :'))
result = multSeries(num)
print(f'Multiplicaton of the series is : {result}','\n')

def squaSeries(sqr):
    sqr = 0
    for i in range(1,num+1):
        sqr = i**i
    return sqr
num = int(input('Enter a number to print power of this number : '))
result = squaSeries(num)
print(f'Square of the {num} number is : {result}')