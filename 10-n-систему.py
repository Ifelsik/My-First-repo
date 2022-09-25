x=int(input("введите целое цисло: "))
n=int(input('в какую псс перевести? '))
s=''
while x!=0:
	r=str(x%n)
	x=x//n
	s+=r
print(s[::-1])
	