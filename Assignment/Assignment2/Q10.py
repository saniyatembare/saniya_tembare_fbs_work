# reverse of the three digit number
num = int(input('Enter three digit number : '))

num1 = num
d1 = num1 % 10
num1 = num1 // 10

d2 = num1 % 10
num1 = num1 // 10

d3 = num1 % 10
num1 = num1 // 10

rev = (d1*100)+(d2*10)+d3

print(f'Three digit reverse number is : {rev}')