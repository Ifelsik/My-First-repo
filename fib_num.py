print('Программа выводит n-ый член последовательности Фибоначчи')
n=int(input())
f=1
c=1
k=0
if n==1 or n==2:
	print(f)
while k!=n:
	d=f
	f=f+c
	c=d
	k+=1
	print(f, end=' ')
print()
print(f)	