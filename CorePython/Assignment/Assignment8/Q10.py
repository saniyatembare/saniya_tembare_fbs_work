# Write a program to check if entered year is a leap year or not. 

def leapYear(yr):

    if(yr % 4 == 0):
        return True
    
year = int(input('Enter a year to check leap or not : '))
result = leapYear(year)
if(result == True):
    print(f'{year} is leap Year')
else:
    print(f'{year} is not leap Year')