n=int(input())
k=0
a=30
for i in range(n):
      if i%2==0:
      	print(a*" ", "*  ****")
      	print(a*" ", "*  *")
      	print(a*" ", "*  *")
      	print(a*" ", "*"*7)
      	print(a*" ","   *  *")
      	print(a*" ","   *  *")
      	print(a*" ","****  *")
      	print()
      elif i%2!=0:
      	print(a*" ","    *")
      	print(a*" ", "   *")
      	print(a*" ","  *   *")
      	print(a*" ","   * * *")
      	print(a*" ", "*   *   *")
      	print(a*" "," * * *")
      	print(a*" ","  *   *")
      	print(a*" ", "     *")
      	print(a*" ", "    *\t")
      	print()
      k=k+1