a, b=int(input('Программа находит НОК и НОД чисел\nВведите число a: ')), int(input('Введите число b: '))
b1=b
a1=a
if a>b:
	q=a//b
	r=a-b*q
	while r!=0:
		q=b//r
		c=r
		r=b-q*r
		b=c
	print('НОК', int(b1*a/b))
	print('НОД', b)
else:
	q=b//a
	r=b-a*q
	while r!=0:
		q=a//r
		c=r
		r=a-q*r
		a=c			
	print('НОК',int(a1*b/a))
	print('НОД',a)				
if b==1:
	print('Числа взаимно простые')					