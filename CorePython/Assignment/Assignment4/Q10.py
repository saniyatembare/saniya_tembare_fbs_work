#  WAP to check if given number is Perfect Number. 
n = int(input('Enter a number to check perfect or not : '))
sum = 0
for i in range(1,n):
    if(n % i == 0):
        sum += i
if(sum == n):
    print(f'{n} is perfect')
else:
    print(f'{n} is not perfect')