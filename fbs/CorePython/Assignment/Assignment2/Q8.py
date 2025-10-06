# swap two numbers
x = int(input('Enter the number1 : '))
y = int(input('Enter the number2 : '))

print(f'Before swapping number x is {x}, and y is {y}')

z = x
x = y
y = z
print(f'After swapping number x is {x}, and y is {y}')