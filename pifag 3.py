import math
for n in range(2,2000):
	a=math.sqrt((n+1)**2-(n-1)**2)
	if a==int(a):
		print(n-1,int(a),n+1)