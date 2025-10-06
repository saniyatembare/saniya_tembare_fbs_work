#Sum of three digit number 
num = int(input('Enter the three digit number : '))

num1 = num
d1 = num1 % 10
num1 = num1 // 10

d2 = num1 % 10
num1 = num1 // 10

d3 = num1 % 10
num1 = num1 // 10

sum = d1 + d2 + d3

print(f'Sum of the three digit number is : {sum}')