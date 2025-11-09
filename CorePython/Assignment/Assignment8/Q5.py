# Sum of all prime numbers between 1 to n

def sumPrime():
    start = int(input('Enter a starting number : '))
    end = int(input('Enter a ending number : '))
    sum = 0
    for i in range(start,end+1):
        for j in range(2,i):
            if(i % j == 0):
                # print(f'{i} Not a prime number ')
                break
        else:
            print(i,end=' ')
            sum = sum + i
    print()
    print(f'{sum} is sum')

sumPrime()