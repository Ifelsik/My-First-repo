a1=input()
a1,a2=="", ""
for i in range (len(a)):
	if a[i]>="0" and a[i]<="9":
		a1+=a[i]
	else:
		a2+=a[i]+" "
		a1+=" "
a3=a1.split()
a4=a2.split()
if len(a3)>len(a4):
	for i in  range (len(a4)):
		if a4[i]==