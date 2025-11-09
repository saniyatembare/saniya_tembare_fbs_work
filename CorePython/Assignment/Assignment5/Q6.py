# Write a program to print prime numbers between 1 to 100. 

start = 1
end = 100
for i in range(1,end+1):
    for j in range(2,i):
        if(i % j == 0):
            break
    else:
        print(i,end=' ')