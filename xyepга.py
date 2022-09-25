s=input()
k=1
i=0
l=len(s)
e,f='',''
while i!=l-1:
    if s[i]==s[i+1]:
        k+=1
    elif s[i]!=s[i+1]:
        c=s[i]
        d=s[i]+str(k)
        f=s.replace(c*k,d)
        k=1
    j=e+f    
    i+=1    
print(j)
			