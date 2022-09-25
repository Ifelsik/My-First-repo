n=int(input())
k=0
for i in range(2,n):
	if n%i==0:
		k=1
		break
if k==1:
	print('составное')	
if k==0 and n!=1:
	print('простое')
if n==1:
	print('единица')			