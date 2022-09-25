import f_div

n=int(input())
for i in range(2,n+1):
	a=f_div.f_div(i)
	if len(a)%2!=0:
		if i**0.5==float(a[int(len(a)/2)]):
			print(i, i**0.5, a, len(a))
		print()
