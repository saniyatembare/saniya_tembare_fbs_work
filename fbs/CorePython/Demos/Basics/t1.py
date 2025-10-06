# Program to find minimum number of notes for given amount
# Denominations: 1000, 500, 100, 50, 20, 10, 5, 1

amount = int(input("Enter the amount: "))

denoms = [500, 200, 100, 50, 20, 10, 5, 1]

# Manual greedy calculation without loops
n1 = amount // denoms[0]
r1 = amount % denoms[0]

n2 = r1 // denoms[1]
r2 = r1 % denoms[1]

n3 = r2 // denoms[2]
r3 = r2 % denoms[2]

n4 = r3 // denoms[3]
r4 = r3 % denoms[3]

n5 = r4 // denoms[4]
r5 = r4 % denoms[4]

n6 = r5 // denoms[5]
r6 = r5 % denoms[5]

n7 = r6 // denoms[6]
r7 = r6 % denoms[6]

n8 = r7 // denoms[7]

# Total minimum notes
total_notes = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8

print("Minimum number of notes needed:", total_notes)