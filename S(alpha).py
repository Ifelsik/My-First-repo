import math
def S(a, alpha):
	A=math.radians(alpha)
	return 2*math.sin(A)*math.sqrt(1-a*a*(math.sin(A)**2))
	
for i in range(19):
	alpha=10*i
	print(S(sqrt(2)/2, alpha))
	print()