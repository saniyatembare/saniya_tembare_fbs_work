# Calculate simple interest 
p = int(input('Enter the principle amount : '))
r = int(input('Enter the rate : '))
t = int(input('Enter the time : '))

SI = (p * r * t) / 100

print(f'Simple interest of the amount is {SI}')
