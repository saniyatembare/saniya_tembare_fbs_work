# num = int(input('Enter a number to ckeck number is prime or not : '))
s = 2
e = 100
for x in range(s,e+1):
    for i in range(2,x):
        if(x % i == 0):
            break
    else:
        print(x, end = ' ')