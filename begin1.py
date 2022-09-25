print ('Удовлетворяет ли точка A(x,y) решению системы неравенств?')
print ('введите x,y')
x, y = map (float,input().split())
if (x*x)+(y*y)>=4 and y<=x and x<=2 and y>0:
	print ("да")
else:
	print ("нет")