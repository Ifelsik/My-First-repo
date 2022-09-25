a, b, c = map(int,input().split())
m=a
if a<b:
	m=b
	if m >c:
		print (m)
	else :
		print (c)