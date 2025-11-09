#Using third variable 
x = 10
y = 20
print(f'Befor swapping x is {x}, and y is {y}')
z = x
x = y
y = z
print(f'After swapping x is {x}, and y is {y}')

#Without using third variable
a = 10
b = 20
print(f'Before swapping x is {a}, and y is {b}')
a = a + b
b = a - b
a = a - b
print(f'After swapping x is {a}, and y is {b}')

#Eassy way
p = 10
r = 20
print(p,r)
p,r = r,p
print(p,r)