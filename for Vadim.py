n=96
A=[]
B=[]
C=[]
for n in range(1,33):
	k=3*n-1
	if n!=11:
		if n%2!=0:
			A.append(k-1)
			B.append(k)
			C.append(k+1)
		else:
			A.append(k+1)
			B.append(k)
			C.append(k-1)
	else:
			A.append(k-1),A.append(k), A.append(k+1)
B.append(97)
C.append(98)
print(A)
print()
print(B)
print()
print(C)
	