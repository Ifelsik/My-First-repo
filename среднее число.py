print ('Программа найдет среднее число')
a, b, c=map(int,input('введите 3 значения ').split())
if a==b or a==c or b==c:
	print('Среднего числа нет')	
elif a>b:
	if a<c:
		print(a)
	elif a>c:
		if c>b:
			print(c)
		else:
			print(b)		
elif a<b:
	if a>c:
		print(a)
	elif a<c:
		if b>c:
			print(c)
		else:
			print(b)	
								
			