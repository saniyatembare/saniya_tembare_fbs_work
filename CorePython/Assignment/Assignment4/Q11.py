# WAP to check if given number Strong Number.
num = int(input("Enter a number: "))
n = num
sum = 0

while(n != 0):
    # compute factorial of digit manually
    digit = n % 10
    n = n // 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum += fact

if(sum == num):
    print(num, "is a Strong Number")
else:
    print(num, "is Not a Strong Number")