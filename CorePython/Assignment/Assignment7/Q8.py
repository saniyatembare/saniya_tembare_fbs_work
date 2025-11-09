k = 7
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    
    for s in range(1,k+1):
        print(' ',end=' ')
    k -= 2

    for j in range(1,i+1):
        if(j != 5):
            print(i-j+1,end=' ')
    print()