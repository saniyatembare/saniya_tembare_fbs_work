s=1
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')

    a = 1
    for j in range(1,s+1):
        print(a,end=' ')
        a+=1
    s+=2
    print()