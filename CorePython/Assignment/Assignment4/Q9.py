# WAP to print all numbers in a range divisible by a given number. 
start = int(input('Enter a starting number : '))
end = int(input('Enter a ending number : '))
divisor = int(input('Enter a divisiblity number : '))

for i in range(start,end + 1):
    if(i % divisor == 0):
        print(i)