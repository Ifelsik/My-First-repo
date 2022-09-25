b=int(input())
a=b
i=2
c=0
while b!=1:
	if b%i==0:
		for j in range (2,i):
			if i%j==0:
				c=1
				break
		if c==0:
			b=b/i
			print(i,end=" ")
			if b!=1:
				print("×",end=" ")
			if b%i==0:
				i-=1
	i+=1
print("=",a)
	
				
	