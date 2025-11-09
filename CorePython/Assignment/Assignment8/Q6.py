# Write a program to find print the following Fibonacci series using 
# functions: 
# 1  1  2  3 5 8  n terms 

def fiboSeries():
    f = 0
    s = 1
    num = int(input('Enter a number : '))
    for i in range(0,num+1):
        total = f + s
        print(f, end=' ')
        f = s
        s = total
fiboSeries()