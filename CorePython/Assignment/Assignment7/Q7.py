for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    
    for k in range(2,i+1):
        print(i-k+1,end=' ')
    print() 