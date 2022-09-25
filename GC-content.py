g=input()
k=0
s=0
for c in g.upper():
	if c=='C' or c=='G':
		k+=1
	s+=1	
print(k/s*100)	