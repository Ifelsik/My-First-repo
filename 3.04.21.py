a=[]
s=input()
while not s=='end':
	s=s.split()
	a.append(s)
	s=input()
x=len(a)
y=len(a[0])
b=[[0]*y for i in range (x)]
for j in range (y):
	for i in range(x):
		for k in range(-1,2):
			jk=j+k
			ik=i+k
			if 0 <= jk < y and jk!=j:
				b[j][i]+=int(a[jk][i])
			elif jk!=j:
				b[j][i]+=int(a[y-1][i])
			if 0 <= ik < x and ik!=i:
				b[j][i]+=int(a[j][ik])
			elif ik!=i:
				b[j][i]+=int(a[j][x-1])
print(b)
			
