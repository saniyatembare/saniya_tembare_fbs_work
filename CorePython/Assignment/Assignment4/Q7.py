# WAP to print all integers upto n that aren’t divisible by 2 and 3.
n = int(input('Enter a number : '))
for i in range(1,n):
    if(i % 2 == 0 or i % 3 == 0):
        pass
    else:
        print(i)