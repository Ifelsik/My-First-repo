x, y = map (float,input().split())
if (x*x)+(y*y)<=1:
	if x<=0 or y>=x:
		print ('да')
else:
	print ('нет')