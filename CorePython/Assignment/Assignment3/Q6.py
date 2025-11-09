# Write a program to calculate profit or loss.
cp = int(input('Enter a cost price of the product : '))
sp = int(input('Enter a selling price of the product : '))

if(sp > cp):
    profit = sp - cp
    profit = (profit/cp)*100
    print(f'{profit}% profit')
else:
    loss = cp - sp
    loss = (loss/cp)*100
    print(f'{loss}% Loss')