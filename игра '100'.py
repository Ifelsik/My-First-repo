import random#дописать код
def complay(x):
    if x%11!=1 and x!=1:
        k=(x-1)//11+1
        return 11*k+1-x
    else:
        return random.randint(1,10)


if random.randint(0,1)==1:
    player="человек"
else:
    player='компьютер'
print('первым ходит:',player)

x=0
turn=0
if player=="человек":
    while x<100:
    	x+=int(input('Введите число от 1 до 10:  '))
    	s=complay(x)
    	if x>=100:
    		print('ВЫ ПОБЕДИЛИ!')
    		break
    	x+=s
    	print('компьютер выдал: ', s)
    	if x>=100:
    		print('Вы проиграли')
    	turn+=1
    	print('ХОД' , turn)
else:
	while x<100:
	   	s=complay(x)
	   	x+=s
	   	print('компьютер выдал: ', s)
	   	if x>=100:
	   		print('Вы проиграли')
	   		break
	   	x+=int(input('Введите число от 1 до 10:  '))
	   	if x>=100:
	   		print('ВЫ ПОБЕДИЛИ!!!')
	   	turn+=1
	   	print('ХОД' , turn)
