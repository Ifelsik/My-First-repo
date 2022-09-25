def f_div(x):
	a=[1]
	for i in range(2, x):
		if x%i==0:
			a.append(i)
	a.append(x)
	return a
	
	

