#Calculate area of rectangle and are of triangle
print('Enter the breadth and height of the triangle')
h = int(input('Enter the height of the triangle : '))
b = int(input('Enter the breadth of the triangle : '))

print('Enter the length and width of the rectangle')
l = int(input('Enter the length of the rectangle : '))
w = int(input('Enter the width of the rectangle : '))

area_of_triangle = (1/2) * h * b

area_of_rectangle = l * w

print(f'Area of the triangle is {area_of_triangle}, and Area pf the rectangle is {area_of_rectangle}')