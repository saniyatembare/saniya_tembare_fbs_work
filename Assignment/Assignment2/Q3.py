#convert distance given in feet and inches into meter and centimeter
feet = int(input('Enter feet : '))
inches = int(input('Enter inches : '))

total_meters = (feet * 0.3048) + (inches * 0.0254)

meters = int(total_meters)

centimeters = (total_meters - meters) * 100

print(f'{feet} feet and {inches} inch is {meters} meters and {centimeters} centimeter')