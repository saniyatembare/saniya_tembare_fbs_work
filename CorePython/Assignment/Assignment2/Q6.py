#calculate salary of employee based on basic, da = 10% of basic, ta = 12% of basic, hra = 15% of basic   
salary = int(input('Enter the basic salary : '))

da = (10*salary)/100
ta = (12*salary)/100
hra = (15*salary)/100

Total_salary = salary + da + ta + hra

print(f'Total salary of the employee is : {Total_salary}')