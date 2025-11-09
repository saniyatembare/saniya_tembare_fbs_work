# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle. 
side1 = int(input('Enter 1st side : '))
side2 = int(input('Enter 2nd side : '))
side3 = int(input('Enter 3rd side : '))

if(side1 > 0 and side2 > 0 and side3 > 0):
    if(side1 == side2 and side2 == side3 and side3 == side1):
        print('Triangle is Equilateral')
    elif(side1 == side2 or side2 == side3 or side3 == side1):
        print('Triangle is Isosceles')
    else:
        print('Triangle is Scalene')
else:
    print('Triangle is not valid')