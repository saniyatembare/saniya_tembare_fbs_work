s=1
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')

    for j in range(1,s+1):
        print(chr(64+j),end=' ')
    s+=2
    print()