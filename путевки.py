a=[]
i,j,k=0,0,0
mx=0
for x in range(100):
	for y in range(51):
		for z in range(34):
				if 21*x+40*y+60*z==2000:
					d=15*x+27*y+45*z
					if d>mx:
						mx=d
						i=x
						j=y
						k=z
print(i, j, k)