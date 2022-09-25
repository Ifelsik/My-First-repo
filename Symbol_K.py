a=input()
e=0
for j in range (len(a)):
	if a[j]!="@":
		e=a[j]
		break
for i in range (len(a)):
	if a[i]!="@":
		if j!=i:
			e=e+a[i]
if e==0:
	s=1
else:
	print(e)		