# Write a program to print first n prime numbers. 

num = int(input('Enter number to print prime number : '))
total = 0
n = 2
while(total < num):
    for i in range(2, n):
        if(n % i == 0):
            break
    else:
        print(n,end=' ')
        total += 1
    n += 1