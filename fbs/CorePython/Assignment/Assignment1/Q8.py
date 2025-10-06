#program to convert days into years weeks and days 
ndays = int(input('Enter days : '))

#perform operation
years = ndays // 365

days = ndays % 365

weeks = days // 7

days = days % 7

#display the result
print(f'In {ndays} there are {years} years, {weeks} weeks, and {days} days.')