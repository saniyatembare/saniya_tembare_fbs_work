# WAP to print Fibonacci series upto n.
n = int(input('Enter a number to print fibonacies series : '))
f = 0
s = 1
for i in range(0,n):
    next = f + s
    print(f)
    f = s
    s = next