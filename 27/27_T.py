f=open('27_T.txt')
a=f.readlines()
print(a)
b=[]
for i in range (len(a)):
	x=int(a[i])
	r=x%6
	for j in range (i+1, len(a)):
		y=int(a[j])
		if 6-r==(y%6):
			b.append(x+y)
print(b)
			
		