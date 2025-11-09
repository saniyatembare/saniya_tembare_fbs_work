#Take two input angles and find third angle of triangle
a = float(input('Enter 1st angle of triangle : '))
b = float(input('Enter 2nd angle of triangle : '))

#perform operation
angle = 180 - (a + b)

#display the result
print(f'Third angle of triangle is {angle}')