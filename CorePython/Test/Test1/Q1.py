#Find the area of perimeter of following figure (accept the length, breadth, and radius)

length = float(input('Enter the length of perimeter : '))
breadth = float(input('Enter the breadth of the perimeter : '))
radius = float(input('Enter the radius of the perimeter : '))

area = length * breadth

semicircle = (3.14 * radius ** 2) / 2

perimeter = area + semicircle

print(f'Area of the perimeter is {perimeter}')