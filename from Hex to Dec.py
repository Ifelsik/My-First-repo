a=[0]*91
k=0
for i in range (48,91):
	if 48<=i<=57:
		a[i]=k
		k+=1
	if 65<=i<=90:
		a[i]=k
		k+=1

x=input()
x=x[::-1]
digit=0
dec=0
for i in range(len(x)):
	dec+=a[ord(str.upper(x[i]))]*16**digit
	digit+=1
print(dec)
	
	

		
	