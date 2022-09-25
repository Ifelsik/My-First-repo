a=input()
if len(a)>1:
	h=a[0]
	for i in range (1,len(a)):
		if i%3!=0:
			h=h+a[i]
	print(h[1:len(a)])