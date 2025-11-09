# WAP to print sum of series upto n.
sum = 0
n = int(input('Enter number to print sum of numbers : '))
for i in range(1,n+1):
    sum = sum + i
print(sum)