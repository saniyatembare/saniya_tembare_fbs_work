#Take two numbers to find quotint and remainder
divident = float(input('Enter the divident : '))
divisor = float(input('Enter the divisor : '))

#perform operatiom
remainder = divident % divisor
quotient = divident // divisor

#Display result
print(f'{quotient} is quotient and {remainder} is remainder')