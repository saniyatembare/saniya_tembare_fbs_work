#Calculate the cost of painting the following building wall (both interior and exterior). You need to accept
# area of one wall and cost of both interior and exterior wall

area = int(input('Enter the area of one wall : '))
inner_cost = int(input('Enter the interior cost : '))
outer_cost = int(input('Enter the exterior cost : '))

inner_wall = 8
outer_wall = 7

Total_inner = inner_wall * area * inner_cost
Total_outer = outer_wall * area * outer_cost
Total = Total_inner + Total_outer

print(f'Interior wall cost is {Total_inner}, and Exterior wall cost is {Total_outer}, and the Total cost is {Total}')