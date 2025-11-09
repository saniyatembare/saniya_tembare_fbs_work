# WAP to print factorial of a number .
n = int(input('Enter number to print factorial : '))
mul = 1
for i in range(1,n+1):
    mul *= i
print(mul)