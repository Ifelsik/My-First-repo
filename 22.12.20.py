a=input()
n=0
s=0
for i in  range(len(a)):
	if a[i]=="+":
		b=a[n:i]
		s=s+int(b)
		n=i+1
print(s+int(a[a.rfind("+"):len(a)]))
