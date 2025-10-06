#calculate simple intrest using principle rate and time
p = float(input('Enter principle amount : '))
r = float(input('Enter rate : '))
t = float(input('Enter time : '))

#perform operation
SI = p*t*r/100

#display result
print(f'Simple interest is {SI}.')