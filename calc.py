print('Калькулятор\nДопустимые операции:\n+(сложение)\n‐(вычитание)\n*(умножение)\n/(деление)\nmod(остаток от деления)\ndiv(целочисленное деление)\npow(возведение в степень)')
a=float(input('\nВведите число: '))
o=str(input('Какую операцию вы хотите соверштиь? '))
b=float(input('Введите число:'))
if o=='+':
	print(a+b)
elif o=='-':
	print(a-b)
elif o=='*':
	print(a*b)
elif o=='/':
	if b==0:
		print('Деление на 0!')
	else:
		print(a/b)			
elif o=='mod':
	if b==0:
		print('Деление на 0!')
	else:
		print(a%b)
elif o=='pow':
	print(a**b)
elif o=='div':
	if b==0:
		print('Деление на 0!')
	else:	
		print(a//b)
else:
	print('Недопустимая операция!')			