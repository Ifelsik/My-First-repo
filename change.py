def modify_list(lst):
	l=len(lst)
	i=0
	while i<l:
		if lst[i]%2==0:
			lst[i]=lst[i]//2
			i+=1
		else:
			del lst[i]
			l-=1
lst=list(map(int,input().split()))
modify_list(lst)
	

