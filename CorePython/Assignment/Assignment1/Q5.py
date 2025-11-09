#calculate the compound interest using principle rate and time
p = float(input('Enter the principle : '))
r = float(input('Enter the rate : '))
t = float(input('Enter the time : '))

#Perform operation 
CI = p*(1+r/100)-p

#display the result
print(f'Compound intrest is {CI}')