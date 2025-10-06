#calculate selling price of book on cost price and discount
cost_price = int(input('Enter the cost price of the book is : '))
discount = int(input('Enter the discount on the book : '))

discount_amount = (cost_price * discount) / 100

selling_price = cost_price - discount_amount

print(f'Selling price of the book is : {selling_price}')