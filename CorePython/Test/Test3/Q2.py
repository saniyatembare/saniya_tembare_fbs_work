n = int(input("Enter n: "))
fact = 1.0
total = 0.0

for i in range(1, n+1):
    fact *= i          
    total += i / fact  

print(f"Sum of series up to {n} = {total}")
