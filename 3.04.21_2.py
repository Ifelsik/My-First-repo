n=int(input())
a=[[0]*n for i in range (n)]
a[0][0]=1
s=1
j,i=0,0
q=0
for p in range (1,n**2):
    s+=1
    if q==1 and 0<=j+1<n and a[j+1][i]==0:
        q=1
    else:
        q=0
    for k in range (-1,2):
        c=0
        ik=i+k
        jk=j+k
        if ik!=i:
            if 0<=ik<n and q==0:
                if a[j][ik]==0:
                    a[j][ik]+=s
                    i+=k
                    c=1
        if jk!=j:
            if 0<=jk<n and c==0:
                if a[jk][i]==0:
                    a[jk][i]+=s
                    j+=k
                    q=1
            else:
                q=0
for j in range (n):
    for i in range (n):
        print(a[j][i], end=" ")
    print()
            
