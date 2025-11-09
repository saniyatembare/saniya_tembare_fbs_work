for i in range(1,6):
    for j in range(1,6):
        if(i==j or 2+j==i or (i==5 and j == 1) or i+2==j or (j==5 and i==1)):
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()