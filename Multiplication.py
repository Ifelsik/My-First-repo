a, b, c, d=int(input()), int(input()), int(input()), int(input())
for k in range(c,d+1):
	print (' ',k, end='')
print()
for i in range(a,b+1):	
	print(i, end=' ')
	for j in range(c,d+1):
		print(i*j, end=' ')
	print()	
		