a = float(input('Enter coefficient a: '))
b = float(input('Enter coefficient b: '))
c = float(input('Enter coefficient c: '))

# Calculate the discriminant
D = (b**2 - 4*a*c)**0.5

# Calculate the two roots
root1 = (-b + D) / (2 * a)
root2 = (-b - D) / (2 * a)

print(f'Roots of quadratic equation is {root1} and {root2}')