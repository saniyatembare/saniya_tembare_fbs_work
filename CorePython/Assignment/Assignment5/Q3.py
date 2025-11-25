# Accept no. of passengers from user and per ticket cost. Then accept age of each  
# passenger and then calculate total amount to ticket to travel for all of them based on  
# following condition : 
# a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full. 

# Total_amt = 0
# persons = int(input('Enter a number of persons :'))
# for i in range(1, persons):
#     print(f'Information of person {i}')
#     age = int(input('Enter your age : '))
#     ticket = int(input('Enter ticket amount : '))

#     if(12 < age):
#         discount = 30
        
#     elif(age > 59):
#         discount = 50
        
#     else:
#         discount = 0
        
#     amt = ticket * discount / 100
#     Totalamt = ticket - amt
#     Total_amt += Totalamt
#     print(f'Ticket after discount: {Totalamt}\n')
        
# print(f'Total amount of 5 person ticket is {Total_amt}')

Total_amt = 0
persons = int(input('Enter number of persons: '))

for i in range(1, persons + 1):
    print(f'Information of person {i}')
    age = int(input('Enter age: '))
    ticket = float(input('Enter ticket amount: '))

    if(age < 12):
        discount = 30
    elif(age < 59):
        discount = 50
    else:
        discount = 0

    amt = ticket * discount / 100
    disamt = ticket - amt
    Total_amt += disamt

    print(f'Ticket cost after {discount}% discount: {disamt}\n')

print(f'Total amount for {persons} persons ticket is: {Total_amt}')
