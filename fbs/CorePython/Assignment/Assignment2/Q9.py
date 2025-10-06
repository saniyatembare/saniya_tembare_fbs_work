#Swap two numbers without using third variable 
x = int(input('Enter the number1 : '))
y = int(input('Enter the number2 : '))

print(f'Before swapping numbers x is {x}, and y is {y}')

x = x + y
y = x - y
x = x - y
print(f'After swapping number x is {x}, and y is {y}')