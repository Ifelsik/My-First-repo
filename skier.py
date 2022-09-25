n=float(input())
p=1+(n/100)
a=0
b=0
c=10
while a<200:
	c*=p
	a+=c
	b+=1
print(a)
print(b-1)	