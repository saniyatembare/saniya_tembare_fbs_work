# WAP to check if a given number is prime number or not.
n = int(input('Enter a number to check number is prime or not : '))
for i in range(2,n):
    if(n % 2 == 0):
        print(f'{n} is not prime number')
        break
else:
    print(f'{n} is a prime number')