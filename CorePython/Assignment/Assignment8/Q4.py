# Sum of all odd numbers between 1 to n  

def sumOdd():
    sum = 0
    num = int(input('Enter a number to print addition of odd number : '))
    for i in range(1,num+1):
        if(i % 2 == 0):
            pass
        else:
            print(f'Odd Numbers : {i}')
            sum += i
    print(f'Total sum of odd number is {sum}')
sumOdd()