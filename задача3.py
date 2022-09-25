
def f(x):
	if x>=-8:
		return (abs(x**3+x-3)-x)*((x+8)**0.5-1)/(x**2+x-2)
	else:
		return(1)

s=-100
while s<=100:
	if f(s)<=0:
		print(s)
	s+=.01
	