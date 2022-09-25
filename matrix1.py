n=int(input())
a=[[0]*n for i in range (n)]
for i in range(n):
    for j in range(n):
        if j==(n-1)-i:
            a[i][j]=1
        if a[i-1][j]==1:
            a[i][j]=2
        if a[i-1][j]==2:
            a[i][j]=2
if n==1:
    print(1)
else:
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
            
