import math
def sin(x):
	x=math.radians(x)
	return x-x**3/6+x**5/120-x**7/5040

print(sin(1))	
	